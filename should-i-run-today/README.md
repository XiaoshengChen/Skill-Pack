# Should I Run Today

[中文](README.md) | [English](README.en.md)

一个面向聊天式 agent 的跑步建议 skill：根据 HRV、睡眠、静息心率、运动负荷截图，以及必要的安全红旗问题，给出保守的“今天是否适合跑步”建议。

它不是医疗诊断，也不提供所谓“安全许可”。它只做训练建议，并且在信息不足时默认保守。现实身体不是 dashboard 装饰品，别拿几张图硬凹确定性。

## 它会做什么

- 一次只问一个关键输入，避免把用户淹死在表单里。
- 优先读取 HRV 和睡眠截图。
- 必要时补静息心率或昨天训练负荷。
- 对胸痛、头晕、心悸、近期感染、心脏病史等红旗问题优先 fail closed。
- 最终只给四类结论：
  - `今天不建议跑`
  - `今天只建议轻松活动`
  - `今天可以轻松跑`
  - `今天可以正常跑`

## 安装

把整个目录复制到你的 skills 目录，保留 `agents/`：

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

也可以让 agent 帮你装：

```text
请把 should-i-run-today 安装到我的全局 skills 目录，并保留所有子目录。
```

## 触发方式

用户类似这样问时使用：

```text
今天适合跑步吗？
我今天能跑吗？
今天该不该跑步？
```

skill 会从 HRV 截图开始。如果用户没有截图，会切换到更保守的 fallback 问答。

## 详细说明

完整对话流程、截图解析规则、红旗问题、决策策略和输出模板见：[`SKILL.md`](SKILL.md)。
