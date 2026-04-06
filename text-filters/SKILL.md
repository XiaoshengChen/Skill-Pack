---
name: text-filters
description: Rewrite short Chinese text through a named writing filter by first extracting the sentence's real meaning, then upgrading it with the chosen worldview, sentence logic, and metaphor system, and finally outputting 3 short final versions. Use when the user asks for filters such as 王小波滤镜, 张潇雨滤镜, 鲁迅滤镜, 李诞滤镜, or 特德姜滤镜.
---

# Text Filters

## Overview

Treat each filter as a way of seeing, not a bag of phrases. Extract the sentence's real meaning first, then pass it through the chosen filter's worldview, structural patterns, and sentence texture.

This skill currently supports 5 filters:

- 王小波滤镜
- 张潇雨滤镜
- 鲁迅滤镜
- 李诞滤镜
- 特德姜滤镜

Read these references as needed:

- Shared rules: [references/common-rules.md](references/common-rules.md)
- How to choose a filter: [references/filter-selection.md](references/filter-selection.md)
- Cross-filter demo set: [references/demos.md](references/demos.md)
- 王小波: [references/profiles/wang-xiaobo.md](references/profiles/wang-xiaobo.md)
- 张潇雨: [references/profiles/zhang-xiaoyu.md](references/profiles/zhang-xiaoyu.md)
- 鲁迅: [references/profiles/luxun.md](references/profiles/luxun.md)
- 李诞: [references/profiles/li-dan.md](references/profiles/li-dan.md)
- 特德姜: [references/profiles/ted-chiang.md](references/profiles/ted-chiang.md)

## When To Use

Use this skill when the user says things like:

- `鲁迅滤镜：我今天不想上班。`
- `张潇雨滤镜：AI 产品现在很热闹，但比赛可能还没开始。`
- `鲁迅，张潇雨滤镜：进入高中生也足以做独立研究的时代，仍然让他们用所有时间做题。`
- `推荐滤镜：我今天不想上班。`
- `全部滤镜：我今天不想上班。`

Typical inputs:

- One short sentence
- One rough social post
- One thought that feels flat and needs a stronger lens
- One complaint, observation, or trend note that needs a more distinctive voice

Do not use this skill for:

- Long essays
- Translation only
- Copyediting only
- Generic style polishing with no chosen filter

## Command Modes

Support these short command styles by default:

### 1. 指定单个滤镜

- `鲁迅滤镜：……`
- `王小波滤镜：……`
- `张潇雨滤镜：……`
- `李诞滤镜：……`
- `特德姜滤镜：……`

Output:

- `原句真意`
- the chosen filter
- 3 short final versions
- `推荐版本`

### 2. 指定多个滤镜

- `鲁迅，张潇雨滤镜：……`
- `王小波，李诞，特德姜滤镜：……`

Output:

- `原句真意`
- each chosen filter's result block
- one cross-filter recommendation

### 3. 推荐滤镜

- `推荐滤镜：……`

Output:

- `原句真意`
- recommended filter
- short reason
- 3 short final versions

### 4. 全部滤镜

- `全部滤镜：……`

Output:

- `原句真意`
- all supported filters
- one final recommendation

If the user gives a natural-language request instead of this mini-CLI style, infer the closest mode and continue.

## Core Workflow

Always do this in order:

1. Distill the sentence's `real meaning`
2. Check whether the chosen filter fits the input
3. Read the filter profile
4. Upgrade the meaning using the filter's `pattern_library` and `upgrade_moves`
5. Output 3 short final versions
6. Recommend the strongest one

If there is no real meaning yet, do not fake it. Use the filter's `fallback_mode`.

## Output Contract

Default output order:

1. `原句真意`
2. `使用滤镜`
3. `版本1`
4. `版本2`
5. `版本3`
6. `推荐版本`

Keep explanations short. The value is in the final lines, not in the commentary around them.

## Anti-Failure Rules

- Do not imitate surface tics
- Do not force a filter onto an obviously mismatched input
- Do not turn one sentence into a bloated paragraph
- Do not replace the user's idea with generic wisdom
- Do not output long essays unless the user explicitly asks
- Do not keep writing when one sentence already lands

## Default Standard

Every version should usually be:

- 1-3 sentences
- under 120 Chinese characters when possible
- directly postable
- sharper than the input
- recognizably filtered without becoming parody

Apply this compression test:

`If deleting half the words makes it better, the longer version was fake work.`
