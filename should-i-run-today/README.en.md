# Should I Run Today

[中文](README.md) | [English](README.en.md)

A chat-agent skill for conservative running recommendations. It uses HRV, sleep, resting heart rate, training-load screenshots, and necessary red-flag safety questions to answer: “Should I run today?”

It is not medical diagnosis and does not provide “clearance.” It gives training advice and defaults conservative when evidence is weak. Bodies are not dashboards with nicer fonts; fake certainty is how people do dumb things confidently.

## What It Does

- Asks for one key input at a time instead of dumping a form on the user.
- Prioritizes HRV and sleep screenshots.
- Uses resting heart rate or previous training load only when needed.
- Fails closed on red flags such as chest pain, dizziness, palpitations, recent infection, or cardiac history.
- Produces only four recommendation buckets:
  - `今天不建议跑` — do not run today
  - `今天只建议轻松活动` — light activity only
  - `今天可以轻松跑` — easy run is okay
  - `今天可以正常跑` — normal run is okay

## Installation

Copy the whole directory into your skills directory. Keep `agents/` intact.

### Codex

```bash
mkdir -p ~/.codex/skills
cp -R ./should-i-run-today ~/.codex/skills/
```

### Hermes Agent

```bash
mkdir -p ~/.hermes/skills
cp -R ./should-i-run-today ~/.hermes/skills/
```

Or ask your agent to install it:

```text
Please install should-i-run-today into my global skills directory and keep all subdirectories intact.
```

## Trigger Examples

Use this skill when the user asks something like:

```text
今天适合跑步吗？
我今天能跑吗？
今天该不该跑步？
```

The skill starts with an HRV screenshot. If the user has no screenshot, it switches to a more conservative fallback conversation.

## Full Documentation

See [`SKILL.md`](SKILL.md) for the complete conversation flow, screenshot parsing rules, red-flag questions, decision policy, and output templates.
