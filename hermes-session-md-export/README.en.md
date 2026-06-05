# Hermes Session Markdown Export

[中文](README.md) | [English](README.en.md)

Export Hermes Agent conversations into Markdown files that are easy to archive, search, and drop into a wiki or Obsidian vault.

The workflow is deliberately boring and safe:

1. Use the official `hermes sessions export` command to export JSONL first.
2. Convert each session into one `.md` file.
3. Name files as `YYYYMMDDHHMM-short-summary.md`.

It does not mutate `state.db`. The database is the source of truth, not a place for cowboy archaeology.

## Use Cases

- Export Hermes Agent conversation history.
- Filter by source, such as Feishu / Telegram / CLI.
- Archive sessions into a personal wiki, Obsidian vault, or project record.
- Preserve basic metadata such as tool messages, timestamps, source, and model.

## Installation

Copy the whole directory into your skills directory. Keep `scripts/` intact.

### Hermes Agent

```bash
mkdir -p ~/.hermes/skills
cp -R ./hermes-session-md-export ~/.hermes/skills/
```

### Codex / other skill-aware agents

```bash
mkdir -p ~/.codex/skills
cp -R ./hermes-session-md-export ~/.codex/skills/
```

Or ask your agent to install it:

```text
Please install hermes-session-md-export into my global skills directory and keep the scripts subdirectory intact.
```

## Quick Usage

Export all sessions:

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py
```

Export Feishu sessions only:

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py --source feishu
```

Export one session:

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py --session-id SESSION_ID
```

Default output:

```text
~/wiki/hermes-exports/markdown/
```

Fallback if `~/wiki` does not exist:

```text
~/Documents/hermes-session-markdown/
```

## Full Documentation

See [`SKILL.md`](SKILL.md) for the complete workflow, options, filename rules, and verification checklist.
