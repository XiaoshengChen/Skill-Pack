---
name: hermes-session-md-export
description: Use when exporting Hermes Agent conversation sessions to Markdown files. Exports official JSONL first via `hermes sessions export`, then converts each session into one `.md` file named by session start time plus a short summary.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, sessions, export, markdown, archival]
    related_skills: [hermes-agent, obsidian]
---

# Hermes Session Markdown Export

## Overview

Use this skill to export Hermes Agent conversations into human-readable Markdown archives.

The workflow is deliberately boring and safe:

1. Discover where Hermes session state lives.
2. Export sessions with the official CLI to JSONL.
3. Convert JSONL into one Markdown file per session.
4. Report the exact output directory and file count.

Do **not** read or mutate `state.db` directly unless the CLI export is unavailable. The database is the source of truth; `hermes sessions export` is the sane extraction path. Direct SQLite fiddling is how people turn archives into crime scenes.

## When to Use

Use when the user asks to:

- Export all Hermes conversations.
- Export Feishu / Telegram / CLI sessions.
- Save Hermes sessions as Markdown.
- Archive conversations into a wiki or Obsidian vault.
- Convert Hermes JSONL session exports into per-session `.md` files.

Do not use for:

- Searching past sessions only — use `session_search`.
- Editing/deleting/pruning sessions — use `hermes sessions` commands from `hermes-agent` skill.
- Exporting another Hermes profile unless the user explicitly names that profile.

## Session Store Discovery

Before exporting, discover the active Hermes home and session store. Try these in order:

```bash
printf 'HERMES_HOME=%s\n' "${HERMES_HOME:-$HOME/.hermes}"
hermes sessions stats
ls -lh "${HERMES_HOME:-$HOME/.hermes}/state.db" "${HERMES_HOME:-$HOME/.hermes}/sessions/sessions.json" 2>/dev/null || true
```

Expected modern default-profile storage:

```text
~/.hermes/state.db              # SQLite session store, source of truth
~/.hermes/state.db-wal          # SQLite WAL, may exist while gateway is active
~/.hermes/sessions/sessions.json # legacy/auxiliary file, not the primary export path
```

Profiles use:

```text
~/.hermes/profiles/<name>/state.db
~/.hermes/profiles/<name>/sessions/sessions.json
```

If `hermes sessions stats` works, continue. If Hermes CLI cannot find sessions and none of the paths above exist, then ask the user for the Hermes home/profile path. Do not guess across random directories.

## Default Output Directory

Use this default output location:

```text
~/wiki/hermes-exports/markdown/
```

If `~/wiki` does not exist, use:

```text
~/Documents/hermes-session-markdown/
```

Always tell the user the final absolute path after export.

## Filename Rule

Each session becomes one Markdown file.

Filename format:

```text
YYYYMMDDHHMM-摘要20字以内.md
```

Rules:

- Time comes from session `started_at` / start timestamp.
- Summary is at most 20 visible characters.
- Prefer session title as summary.
- If title is missing, use the first user message.
- Remove filename-hostile characters like `/`, `:`, `*`, `?`, quotes, angle brackets, pipe, and control characters.
- If duplicate filenames occur, append `-<session_id_prefix>`.

Example:

```text
202606041736-Hermes对话导出.md
```

## One-Shot Export Commands

### Export everything

```bash
python3 ~/.hermes/skills/autonomous-ai-agents/hermes-session-md-export/scripts/export_hermes_sessions_md.py
```

### Export only Feishu sessions

```bash
python3 ~/.hermes/skills/autonomous-ai-agents/hermes-session-md-export/scripts/export_hermes_sessions_md.py --source feishu
```

### Export one session by ID

```bash
python3 ~/.hermes/skills/autonomous-ai-agents/hermes-session-md-export/scripts/export_hermes_sessions_md.py --session-id SESSION_ID
```

### Test with the shortest Feishu session

```bash
python3 ~/.hermes/skills/autonomous-ai-agents/hermes-session-md-export/scripts/export_hermes_sessions_md.py \
  --source feishu \
  --pick-shortest \
  --min-messages 1 \
  --limit 1 \
  --output /tmp/hermes-session-md-test
```

## Agent Workflow

When the user asks you to perform an export:

1. Check Hermes session stats and store location:
   ```bash
   hermes sessions stats
   ls -lh "${HERMES_HOME:-$HOME/.hermes}/state.db" "${HERMES_HOME:-$HOME/.hermes}/sessions/sessions.json" 2>/dev/null || true
   ```
2. Run the script with the requested filters.
3. Verify Markdown files were written:
   ```bash
   find OUTPUT_DIR -type f -name '*.md' | wc -l
   ```
4. Read one small output file or list a few filenames to sanity-check naming.
5. Report:
   - JSONL export path
   - Markdown output directory
   - number of sessions converted
   - filters used, if any

## Markdown Shape

The script writes each file as:

```markdown
# <summary>

- session_id: `<id>`
- source: `<source>`
- started_at: `<timestamp>`
- last_active: `<timestamp>`
- model: `<model>`
- message_count: `<n>`

---

## user · <timestamp>

...

## assistant · <timestamp>

...

## tool · <timestamp>

...
```

Tool messages are preserved but compacted when content is empty. This keeps the archive readable without pretending tool calls never happened.

## Common Pitfalls

1. **Trying to parse `state.db` directly first.** Don't. Use `hermes sessions export`; direct SQLite is fallback only.
2. **Assuming `~/.hermes/sessions/` has Markdown.** It does not. Modern Hermes stores sessions in `state.db`; `sessions.json` may be legacy/auxiliary.
3. **Exporting another profile accidentally.** Use `hermes -p <profile> sessions export ...` only when the user explicitly asks for that profile.
4. **Forgetting to report output path.** The user asked for files, not vibes. Always give the absolute directory.
5. **Letting giant tool outputs ruin readability.** Keep message content intact by default, but summarize empty tool-call shells by tool name.
6. **Filename summaries longer than 20 characters.** Hard cap it.

## Verification Checklist

- [ ] `hermes sessions stats` succeeded or a valid Hermes home/profile path was found.
- [ ] JSONL export was created by `hermes sessions export`.
- [ ] One Markdown file exists per selected session.
- [ ] Filename starts with `YYYYMMDDHHMM-`.
- [ ] Filename summary is ≤ 20 visible characters.
- [ ] At least one exported Markdown file was inspected.
- [ ] Final response tells the user the output directory and file count.
