# Hermes Session Markdown Export

[中文](README.md) | [English](README.en.md)

把 Hermes Agent 的会话导出成适合归档、搜索、放进 wiki / Obsidian 的 Markdown 文件。

它采用一条比较无聊但安全的路线：

1. 用官方 `hermes sessions export` 先导出 JSONL。
2. 再用脚本把每个 session 转成一个 `.md` 文件。
3. 文件名使用 `YYYYMMDDHHMM-20字以内摘要.md`。

不直接碰 `state.db`。数据库是源头，不是你拿来徒手炒菜的锅。

## 适合什么场景

- 导出 Hermes Agent 的历史对话。
- 按来源导出，比如 Feishu / Telegram / CLI。
- 把会话沉淀到个人 wiki、Obsidian 或长期项目档案。
- 想保留 tool message、时间、source、model 等基本元数据。

## 安装

把整个目录复制到你的 skills 目录，必须保留 `scripts/`：

### Hermes Agent

```bash
mkdir -p ~/.hermes/skills
cp -R ./hermes-session-md-export ~/.hermes/skills/
```

### Codex / 其他支持 skills 的 agent

```bash
mkdir -p ~/.codex/skills
cp -R ./hermes-session-md-export ~/.codex/skills/
```

也可以让 agent 帮你装：

```text
请把 hermes-session-md-export 安装到我的全局 skills 目录，并保留 scripts 子目录。
```

## 快速使用

导出全部 session：

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py
```

只导出 Feishu：

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py --source feishu
```

导出单个 session：

```bash
python3 ~/.hermes/skills/hermes-session-md-export/scripts/export_hermes_sessions_md.py --session-id SESSION_ID
```

默认输出到：

```text
~/wiki/hermes-exports/markdown/
```

如果没有 `~/wiki`，回退到：

```text
~/Documents/hermes-session-markdown/
```

## 详细说明

完整 workflow、参数、文件名规则和验证清单见：[`SKILL.md`](SKILL.md)。
