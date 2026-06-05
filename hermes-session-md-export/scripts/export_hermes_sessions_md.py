#!/usr/bin/env python3
"""Export Hermes sessions to one Markdown file per session.

Pipeline: `hermes sessions export` JSONL -> Markdown files.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

BAD_FILENAME = re.compile(r'[\\/:*?"<>|\x00-\x1f]+')
WS = re.compile(r"\s+")


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def visible_truncate(s: str, n: int = 20) -> str:
    s = WS.sub("", s or "")
    return s[:n] or "未命名会话"


def filename_safe(s: str) -> str:
    s = BAD_FILENAME.sub("-", s)
    s = s.strip(" .-")
    return s or "未命名会话"


def parse_time(value: Any) -> dt.datetime | None:
    if not value:
        return None
    if isinstance(value, (int, float)):
        try:
            return dt.datetime.fromtimestamp(value)
        except Exception:
            return None
    s = str(value).strip()
    if not s:
        return None
    s2 = s.replace("Z", "+00:00")
    # Handle common SQLite-ish timestamp variants.
    for candidate in (s2, s2.split(".")[0] if "." in s2 and "+" not in s2 else s2):
        try:
            parsed = dt.datetime.fromisoformat(candidate)
            if parsed.tzinfo:
                parsed = parsed.astimezone().replace(tzinfo=None)
            return parsed
        except Exception:
            pass
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return dt.datetime.strptime(s[:19], fmt)
        except Exception:
            pass
    return None


def time_prefix(sess: dict[str, Any]) -> str:
    t = parse_time(sess.get("started_at") or sess.get("created_at") or sess.get("last_active"))
    if t is None:
        return "000000000000"
    return t.strftime("%Y%m%d%H%M")


def first_user_text(sess: dict[str, Any]) -> str:
    for m in sess.get("messages") or []:
        if m.get("role") == "user" and m.get("content"):
            return str(m.get("content"))
    for m in sess.get("messages") or []:
        if m.get("content"):
            return str(m.get("content"))
    return "未命名会话"


def summary(sess: dict[str, Any]) -> str:
    return filename_safe(visible_truncate(sess.get("title") or first_user_text(sess), 20))


def md_escape_heading(s: str) -> str:
    return str(s or "").replace("\n", " ").strip()


def message_content(m: dict[str, Any]) -> str:
    content = m.get("content")
    if content:
        return str(content).strip()
    tool_name = m.get("tool_name")
    if tool_name:
        return f"[tool call/result: {tool_name}]"
    calls = m.get("tool_calls")
    if calls:
        try:
            names = []
            for c in calls:
                fn = c.get("function") or {}
                names.append(fn.get("name") or c.get("name") or "tool")
            return "[tool calls: " + ", ".join(names) + "]"
        except Exception:
            return "[tool calls]"
    reasoning = m.get("reasoning") or m.get("reasoning_content")
    if reasoning:
        return str(reasoning).strip()
    return ""


def write_markdown(sess: dict[str, Any], outdir: pathlib.Path, used: set[str]) -> pathlib.Path:
    sid = str(sess.get("id") or sess.get("session_id") or "unknown")
    summ = summary(sess)
    base = f"{time_prefix(sess)}-{summ}"
    name = f"{base}.md"
    if name in used or (outdir / name).exists():
        name = f"{base}-{sid[:8]}.md"
    used.add(name)
    path = outdir / name

    title = sess.get("title") or summ
    parts: list[str] = [
        f"# {md_escape_heading(title)}",
        "",
        f"- session_id: `{sid}`",
        f"- source: `{sess.get('source') or ''}`",
        f"- started_at: `{sess.get('started_at') or ''}`",
        f"- last_active: `{sess.get('last_active') or ''}`",
        f"- model: `{sess.get('model') or ''}`",
        f"- message_count: `{sess.get('message_count') or len(sess.get('messages') or [])}`",
        "",
        "---",
        "",
    ]
    for m in sess.get("messages") or []:
        if m.get("active") is False:
            continue
        role = m.get("role") or "unknown"
        ts = m.get("timestamp") or ""
        content = message_content(m)
        if not content:
            continue
        parts.extend([f"## {role} · {ts}", "", content, ""])

    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return path


def default_output() -> pathlib.Path:
    home = pathlib.Path.home()
    wiki = home / "wiki"
    if wiki.exists():
        return wiki / "hermes-exports" / "markdown"
    return home / "Documents" / "hermes-session-markdown"


def discover_store() -> tuple[pathlib.Path, list[str]]:
    hermes_home = pathlib.Path(os.environ.get("HERMES_HOME", str(pathlib.Path.home() / ".hermes"))).expanduser()
    candidates = [hermes_home / "state.db", hermes_home / "sessions" / "sessions.json"]
    found = [str(p) for p in candidates if p.exists()]
    return hermes_home, found


def main() -> int:
    ap = argparse.ArgumentParser(description="Export Hermes sessions to per-session Markdown files.")
    ap.add_argument("--source", help="Filter by source, e.g. feishu, cli, cron")
    ap.add_argument("--session-id", help="Export a specific session ID")
    ap.add_argument("--output", type=pathlib.Path, default=default_output(), help="Markdown output directory")
    ap.add_argument("--jsonl", type=pathlib.Path, help="Keep/use this JSONL path instead of a temp file")
    ap.add_argument("--limit", type=int, help="Limit converted sessions after filters/sorting")
    ap.add_argument("--min-messages", type=int, default=0, help="Skip sessions with fewer active non-empty messages")
    ap.add_argument("--pick-shortest", action="store_true", help="Sort selected sessions by message count ascending")
    ap.add_argument("--keep-jsonl", action="store_true", help="Keep temp JSONL export and report path")
    args = ap.parse_args()

    hermes = shutil.which("hermes")
    if not hermes:
        print("ERROR: `hermes` CLI not found in PATH.", file=sys.stderr)
        return 2

    hermes_home, stores = discover_store()
    stats = run([hermes, "sessions", "stats"])
    if stats.returncode != 0:
        print("ERROR: `hermes sessions stats` failed.", file=sys.stderr)
        print(stats.stderr or stats.stdout, file=sys.stderr)
        print(f"Checked HERMES_HOME={hermes_home}", file=sys.stderr)
        print(f"Found stores: {stores or 'none'}", file=sys.stderr)
        return stats.returncode or 1

    if args.jsonl:
        jsonl_path = args.jsonl.expanduser().resolve()
        jsonl_path.parent.mkdir(parents=True, exist_ok=True)
        keep_jsonl = True
    else:
        fd, tmp = tempfile.mkstemp(prefix="hermes-sessions-", suffix=".jsonl")
        os.close(fd)
        jsonl_path = pathlib.Path(tmp)
        keep_jsonl = args.keep_jsonl

    cmd = [hermes, "sessions", "export"]
    if args.source:
        cmd += ["--source", args.source]
    if args.session_id:
        cmd += ["--session-id", args.session_id]
    cmd.append(str(jsonl_path))
    exp = run(cmd)
    if exp.returncode != 0:
        print("ERROR: export failed:", file=sys.stderr)
        print(exp.stderr or exp.stdout, file=sys.stderr)
        return exp.returncode or 1

    sessions: list[dict[str, Any]] = []
    with jsonl_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                sessions.append(json.loads(line))

    if args.min_messages > 0:
        def active_content_count(s: dict[str, Any]) -> int:
            return sum(
                1
                for m in (s.get("messages") or [])
                if m.get("active") is not False and message_content(m)
            )
        sessions = [s for s in sessions if active_content_count(s) >= args.min_messages]

    if args.pick_shortest:
        sessions.sort(key=lambda s: (len(s.get("messages") or []), len(first_user_text(s))))
    if args.limit is not None:
        sessions = sessions[: max(args.limit, 0)]

    outdir = args.output.expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    used: set[str] = set()
    files = [write_markdown(s, outdir, used) for s in sessions]

    if not keep_jsonl and not args.jsonl:
        try:
            jsonl_path.unlink()
        except OSError:
            pass

    print("Hermes session Markdown export complete")
    print(f"HERMES_HOME: {hermes_home}")
    print(f"Session stores found: {', '.join(stores) if stores else 'none'}")
    print(f"JSONL: {jsonl_path if (keep_jsonl or args.jsonl) else 'temporary deleted after conversion'}")
    print(f"Output directory: {outdir}")
    print(f"Sessions converted: {len(files)}")
    if files:
        print("Sample files:")
        for p in files[:5]:
            print(f"- {p}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
