# xiaosheng-skills

Reusable AI-agent skills by **Xiaosheng Chen / 陈小胜**.

This repo is a small personal skill library: not a marketplace, not a prompt dump. Each skill is meant to encode a repeatable workflow an agent can actually use.

[中文](#中文) | [English](#english)

---

## 中文

### Skills

| Skill | 简介 | 详细说明 |
|---|---|---|
| `shift-mind` | 把一句话按不同思想滤镜重写成可直接发布的短文本；重点不是“润色”，而是 worldview、句法和隐喻系统的切换。 | [中文 README](shift-mind/README.md) / [English README](shift-mind/README.en.md) |
| `should-i-run-today` | 根据 HRV、睡眠、静息心率、运动负荷截图和安全红旗问题，给出保守的“今天是否适合跑步”建议。 | [中文 README](should-i-run-today/README.md) / [English README](should-i-run-today/README.en.md) |
| `hermes-session-md-export` | 将 Hermes Agent 会话先通过官方 CLI 导出为 JSONL，再转换成按时间和摘要命名的 Markdown 文件，适合归档到 wiki / Obsidian。 | [中文 README](hermes-session-md-export/README.md) / [English README](hermes-session-md-export/README.en.md) |

### 安装

推荐方式：把目标 skill 的整个文件夹复制到你的 agent skills 目录。不要只复制 `SKILL.md`，很多 skill 还依赖 `references/`、`scripts/`、`agents/` 等文件夹。

#### Codex

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
cp -R ./shift-mind ~/.codex/skills/
cp -R ./should-i-run-today ~/.codex/skills/
cp -R ./hermes-session-md-export ~/.codex/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse .\shift-mind "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse .\should-i-run-today "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse .\hermes-session-md-export "$env:USERPROFILE\.codex\skills\"
```

#### Hermes Agent

macOS / Linux:

```bash
mkdir -p ~/.hermes/skills
cp -R ./shift-mind ~/.hermes/skills/
cp -R ./should-i-run-today ~/.hermes/skills/
cp -R ./hermes-session-md-export ~/.hermes/skills/
```

也可以只安装单个 skill：

```bash
cp -R ./shift-mind ~/.codex/skills/
```

如果你让 agent 帮你安装，直接说：

```text
请把这个仓库里的 shift-mind / should-i-run-today / hermes-session-md-export 安装到我的全局 skills 目录，并保留所有子目录。
```

---

## English

### Skills

| Skill | Summary | Details |
|---|---|---|
| `shift-mind` | Rewrites a sentence through different intellectual filters into short publishable lines; not polishing, but switching worldview, sentence logic, and metaphor system. | [中文 README](shift-mind/README.md) / [English README](shift-mind/README.en.md) |
| `should-i-run-today` | Gives a conservative “should I run today?” recommendation from HRV, sleep, resting heart rate, training-load screenshots, and red-flag safety questions. | [中文 README](should-i-run-today/README.md) / [English README](should-i-run-today/README.en.md) |
| `hermes-session-md-export` | Exports Hermes Agent sessions via the official JSONL CLI path, then converts them into timestamped Markdown files for wiki / Obsidian archives. | [中文 README](hermes-session-md-export/README.md) / [English README](hermes-session-md-export/README.en.md) |

### Installation

Recommended: copy the entire skill directory into your agent's global skills directory. Do **not** copy only `SKILL.md`; some skills depend on `references/`, `scripts/`, `agents/`, or other files.

#### Codex

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
cp -R ./shift-mind ~/.codex/skills/
cp -R ./should-i-run-today ~/.codex/skills/
cp -R ./hermes-session-md-export ~/.codex/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse .\shift-mind "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse .\should-i-run-today "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse .\hermes-session-md-export "$env:USERPROFILE\.codex\skills\"
```

#### Hermes Agent

macOS / Linux:

```bash
mkdir -p ~/.hermes/skills
cp -R ./shift-mind ~/.hermes/skills/
cp -R ./should-i-run-today ~/.hermes/skills/
cp -R ./hermes-session-md-export ~/.hermes/skills/
```

Install one skill only:

```bash
cp -R ./shift-mind ~/.codex/skills/
```

If you ask an agent to install it, say:

```text
Please install shift-mind / should-i-run-today / hermes-session-md-export from this repo into my global skills directory, keeping all subdirectories intact.
```

---

Canonical links:

- Personal site: https://chenxs.me/
- About / entity page: https://chenxs.me/about/
- LLM guidance: https://chenxs.me/llms.txt
- GitHub profile: https://github.com/XiaoshengChen
