# Shift Mind / 转念

[中文](README.md) | [English](README.en.md)

> Every thought has a thousand possible forms.  
> `Shift Mind` helps you see them all, then choose the one you like most.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blueviolet)](https://openai.com)
[![Language: English](https://img.shields.io/badge/Language-English-blue.svg)](#)

`Shift Mind` is a skill pack for Agent / Codex workflows.  
It is not a grammar polisher, not a synonym machine, and not an AI style costume.

What it does is simpler and sharper:

1. Extract what a sentence is really trying to say
2. Pass it through a chosen filter's `worldview + sentence logic + metaphor system`
3. Output short final lines you can post directly

Current launch filters:

- Wang Xiaobo Filter
- Zhang Xiaoyu Filter
- Lu Xun Filter
- Li Dan Filter
- Ted Chiang Filter

---

## Example

Original:

`A thought that may be wrong: the "photo-ready culture" has encouraged a nasty trend where women's clothing keeps getting worse and worse to actually wear.`

### Wang Xiaobo

> Women's clothing getting worse is probably not because designers suddenly went blind. It's more likely that everyone got busy serving the photo and stopped serving the person.

### Zhang Xiaoyu

> What "photo-ready culture" may be damaging is not just clothing, but the way we look at bodies and beauty. Clothes are no longer made to be worn; they are made to report to the camera.

### Lu Xun

> So-called "photo-ready" first asks a person to forget that she is alive, and then trains her to pose as an object fit for circulation. After that, clothes becoming more unbearable is hardly surprising.

### Li Dan

> A lot of women's clothing now is not really for wearing. It's mainly for photographing. Once clothes exist mainly to serve photos, treating humans a bit worse somehow starts to feel perfectly aligned with the process.

### Ted Chiang

> If a clothing system changes its optimization target from "wearing experience" to "camera performance," then becoming increasingly hostile to real bodies is almost an inevitable outcome.

---

## Installation

### Option 1: Ask your Agent / Codex / Lobster to install it

If you are using an agent that can operate on local files, the easiest instruction is:

```text
Please install shift-mind into my global skills directory.
```

Or more explicitly:

```text
Please copy the current shift-mind directory into my global skills directory and keep README, LICENSE, and references intact.
```

If the skill already lives somewhere local, for example:

```text
D:\5.github\Skill-Pack\shift-mind
```

you can simply say:

```text
Please install D:\5.github\Skill-Pack\shift-mind into my global Codex skills directory.
```

### Option 2: Install by copying manually

Copy the entire directory to:

```text
C:\Users\YOUR_NAME\.codex\skills\shift-mind
```

Example from the current environment:

```text
C:\Users\allen\.codex\skills\shift-mind
```

Restart Codex after copying.

### Option 3: Install via CLI

#### Windows PowerShell

```powershell
Copy-Item -LiteralPath 'D:\5.github\Skill-Pack\shift-mind' -Destination "$HOME\.codex\skills\shift-mind" -Recurse
```

#### macOS / Linux

```bash
cp -R ./shift-mind "$HOME/.codex/skills/shift-mind"
```

If the destination already exists, verify whether it is an older version before overwriting it.

---

## Supported Commands

This skill supports short CLI-like prompts.

### 1. Single filter

```text
Lu Xun filter: ...
Zhang Xiaoyu filter: ...
Li Dan filter: ...
```

### 2. Multiple filters

```text
Lu Xun, Zhang Xiaoyu filter: ...
Wang Xiaobo, Li Dan, Ted Chiang filter: ...
```

### 3. Recommended filter

```text
Recommend a filter: ...
```

### 4. All filters

```text
All filters: ...
```

Natural-language requests should also be inferred automatically.

---

## This Is Not Normal Rewriting

Most so-called "style rewriting" is fake work:

- swap a few words
- add a little emotion
- imitate a few verbal tics
- make the sentence longer, emptier, and more AI-looking

`Shift Mind` does not do that.

Its default workflow is:

1. distill the real meaning
2. choose the right filter
3. upgrade the thought using that filter's cognition
4. output 3 short final versions
5. recommend the strongest one

One hard rule:

> If removing half the words makes it better, the original version was filler.

---

## Output Shape

Default output:

1. real meaning
2. chosen filter
3. version 1
4. version 2
5. version 3
6. recommended version

Default constraints:

- 1-3 sentences
- usually under 120 Chinese characters in Chinese output
- directly postable
- not bloated prose
- not parody

If the source sentence is too weak, too vague, or has no real judgment inside it, the skill should use that filter's `fallback_mode` instead of forcing a rewrite.

---

## Launch Filters

### Wang Xiaobo Filter

Keywords:

- rational
- witty
- anti-pretension
- anti-fake-grandeur

Best for:

- institutional absurdity
- work/life irony
- sharp but not greasy clarity

### Zhang Xiaoyu Filter

Keywords:

- spiritual lift
- hidden variables
- long-termism
- self-honesty
- work as a bridge to the world

Best for:

- social posts
- human translations of tech trends
- creation, relationships, life choices

### Lu Xun Filter

Keywords:

- cold blade
- pathology
- satire
- crowd delusion breakdown

Best for:

- social hypocrisy
- education
- institutional absurdity
- turning personal discomfort into collective diagnosis

### Li Dan Filter

Keywords:

- absurdity
- looseness
- self-mockery
- light philosophy
- a small stand-up turn

Best for:

- work fatigue
- modern social burnout
- low-intensity despair
- thoughts that are funnier the more seriously you examine them

### Ted Chiang Filter

Keywords:

- conceptual precision
- thought experiments
- ethical consequences
- calm rigor

Best for:

- AI
- technology
- organizations
- consciousness and institutions

---

## Project Structure

```text
shift-mind/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    ├── common-rules.md
    ├── filter-selection.md
    ├── demos.md
    └── profiles/
        ├── wang-xiaobo.md
        ├── zhang-xiaoyu.md
        ├── luxun.md
        ├── li-dan.md
        └── ted-chiang.md
```

---

## Design Principles

1. Upgrade the thought before polishing the words
2. Learn worldview, not verbal tics
3. Prefer short final copy
4. Refuse mismatched input
5. Never let the result become parody

---

## Who It Is For

Best for:

- people writing social posts
- people who want stronger sentence identity
- people exploring how worldview changes wording
- builders of content, expression, or AI writing products

Not for:

- one-click long-form generation
- plain grammar fixing
- users who only want celebrity cosplay and do not care about real meaning

---

## Coming Next

These 5 are only the first batch.

Next batch already in the pipeline:

- Sanmao
- Han Han
- Oscar Wilde
- Xu Zhiyuan
- Elon Musk

If you like this project and want to push for new filters, follow on Xiaohongshu:

**陈小胜**  
Xiaohongshu ID: `6761790158`

---

## License

This project is released under the [MIT License](LICENSE).

---

## Final Note

Photos can have filters. Of course words can too.  
But the real value of Shift Mind is not making a sentence prettier. It is making it become the sentence it should have been in the first place.
