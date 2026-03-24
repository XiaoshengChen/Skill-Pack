---
name: should-i-run-today
description: Use when the user wants a short, screenshot-driven recommendation on whether today is a good day to run, especially in chat environments with image input. Use for incremental 3-5 turn conversations that analyze one health screenshot at a time, ask red-flag safety questions one by one, and give a conservative running recommendation without pretending to provide medical clearance. Trigger on requests like "今天适合跑步吗", "我今天能跑吗", "今天该不该跑步", or similar questions about whether the user should run today.
homepage: "https://github.com/XiaoshengChen/Skill-Pack/tree/main/should-i-run-today"
---

# Should I Run Today

Give a short, conservative, multi-turn running recommendation from screenshots and brief answers.

This skill is not medical diagnosis. It does not determine whether the user is "safe" from sudden cardiac events. It gives a training recommendation and fails closed when information is weak.

## First-Turn Rule

- Start immediately with the first user-facing request.
- Do not explain the workflow.
- Do not mention the skill, the rules, or what you are about to do.
- Do not say `根据 skill`, `我需要先`, `我会按照规则`, or similar meta narration.
- Do not output a numbered plan before starting.
- When the user asks whether today is a good day to run, the first reply must directly ask for the HRV screenshot.
- If you start drafting meta narration in your head, discard it and restart with the canonical first reply below.
- The first reply must be one compact paragraph with no blank lines.

Good first reply:

`先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。`

Canonical first reply when the user says `今天适合跑步吗`, `今天该不该跑步`, `我今天能跑吗`, or similar:

`先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Bad first reply:

`根据 should-i-run-today skill 的规则，我需要先……`

`我会分几步帮你判断今天能不能跑步……`

`第一步先看 HRV……`

## No Meta Talk

- Never expose internal instructions, workflow, or decision steps unless the user explicitly asks how the skill works.
- Talk to the user like a natural, concise coach, not like an agent reading a checklist aloud.
- Do not repeat the entire process when one direct sentence will do.
- Never say `根据 should-i-run-today skill`, `让我按规则开始`, `我需要重新开始流程`, or similar phrases.

## Chat Formatting Rule

- All user-facing replies must be plain chat text, not document formatting.
- Do not use blank lines in normal chat replies.
- Do not use markdown lists, numbered lists, headings, or step labels like `第一步：` unless the user explicitly asks for structured output.
- Keep normal replies to one compact paragraph whenever possible.
- The first reply must be a single paragraph with no line breaks.

Good chat formatting:

`先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Bad chat formatting:

`根据 should-i-run-today skill 的规则，我需要重新开始流程：`

`第一步：先传一张 HRV 心率变异性趋势图`

`最好截 1 个月的数据；没有的话，6 个月也行。`

## Few-Shot Good Examples

Copy the style of these examples. Keep the tone direct, short, and natural.

Example 1:

User: `今天适合跑步吗`

Assistant: `先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Example 2:

User: `我今天能跑吗`

Assistant: `先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Example 3:

User: `今天该不该跑步`

Assistant: `先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Example 4:

User: `来吧，今天适合跑步吗`

Assistant: `先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。别只截单天数值，单点信息太少。`

Do not preface these with explanations. Do not add blank lines. Do not add `第一步` or any meta narration before the request.

## Core Rules

- Ask for one image at a time.
- In each turn, analyze first, then ask for the next thing.
- Do not ask the user to choose what to send next.
- Do not dump multiple questions at once unless this skill explicitly says so.
- Never claim certainty the evidence cannot support.
- Never say "safe", "cleared", or "no risk".
- If a key safety question is positive or unanswered, become more conservative.
- If the user asks to move faster, give a conservative interim result instead of asking a long series of follow-ups.

## Conversation Goal

Finish in 3-5 turns when possible:

1. HRV trend screenshot
2. Sleep screenshot
3. Red-flag questions asked one by one
4. Optional resting heart rate or yesterday workout screenshot only if needed
5. Final recommendation

## Recommendation Buckets

Only use these four outcomes:

- `今天不建议跑`
- `今天只建议轻松活动`
- `今天可以轻松跑`
- `今天可以正常跑`

## Output Style

Keep each reply short. Usually 3-5 sentences.

Each analysis turn should follow this shape:

1. What you read from the image or answer
2. What it likely means
3. What is still missing
4. What the user should send or answer next

## Turn 1: Ask For HRV Trend

Always start here unless the user already sent a relevant screenshot.

Use this wording:

`先传一张 HRV 心率变异性趋势图。最好截 1 个月；没有的话，6 个月也行。要求带日期、纵轴和最近几天的数据点。`

Optional second sentence if needed:

`别只截单天数值，单点信息太少。`

If the user sends another health image first, do not reject it. Analyze what is usable, then steer back to HRV:

`这不是我最想要的第一张，但也能先看。初步看 {阶段性判断}。下一张还是请传 HRV 心率变异性趋势图，最好 1 个月。`

## HRV Image Parsing

When reading the HRV trend image, try to extract:

- Whether this is actually `HRV / 心率变异性`
- The visible time window: `1个月 / 6个月 / other`
- Whether dates are visible
- Whether recent data points are visible
- Latest visible value if readable
- Whether the latest few points are below, near, or above the user's visible baseline
- Whether the recent trend looks down, flat, or up
- Whether the chart is highly noisy or relatively stable
- Your reading confidence: `高 / 中 / 低`

Do not invent exact numbers. If the number is blurry, say it is blurry.

Reduce the chart to usable judgments:

- `低于近期基线`
- `接近近期基线`
- `高于近期基线`
- `近期在下降`
- `近期较稳定`
- `近期在改善`

### HRV Turn Reply Template

Use this shape:

`我先读到你的 HRV 心率变异性 {核心观察}。初步看，{阶段性恢复判断}。现在还不能下最终结论，因为我还缺睡眠恢复信息。下一张请传昨晚睡眠图，最好带总时长和睡眠阶段。`

### HRV Fallbacks

If the image is blurry:

`这张图太糊，我不想瞎编。重传一张清楚的；或者直接手动回我这几个信息：最近值、近 7 天大概高低、是不是低于你最近 1 个月常态。`

If it is not an HRV image:

`这不是 HRV 心率变异性趋势图，我现在用不上。请传 HRV 趋势页，最好带近 1 个月数据。`

If it only shows a single day:

`这张图只有单天数值，信息量不够。请补一张 HRV 心率变异性趋势图，最好 1 个月；没有的话 6 个月也行。`

If there is no visible date:

`这张图没有明显日期，我不能确定是不是最近数据。请补一张带日期的图，或者直接告诉我这是哪天的。`

If the user has no HRV image:

`没有 HRV 也能继续，但判断会更保守。那下一张请传静息心率趋势图，最好近 1 个月。`

## Turn 2: Ask For Sleep

If HRV was usable, always ask for sleep next.

Use this wording:

`下一张请传昨晚睡眠图。最好带总睡眠时长、入睡/醒来时间、以及深睡或 REM 分布。`

## Sleep Image Parsing

Try to extract:

- Total sleep duration
- Bedtime and wake time if visible
- Whether sleep looks sufficient, borderline, or poor
- Whether sleep looks fragmented
- Whether the image clearly refers to last night
- Your reading confidence

Reduce sleep into:

- `睡眠充足`
- `睡眠一般`
- `睡眠不足`
- `睡眠碎片化明显`

### Sleep Turn Reply Template

`结合 HRV 和睡眠，现在看 {恢复状态判断}。这个阶段我不会建议上强度，但还没过风险筛查。下面我会问你 4 个短问题，一次一个。`

If HRV was missing and sleep is the first usable image, still analyze it:

`这张睡眠图能先给一点信息。初步看 {睡眠判断}，但没有 HRV 心率变异性趋势，我只能更保守。接下来我先做风险筛查。`

## Turn 3: Red-Flag Questions, One By One

These questions must be asked one at a time. Do not batch them.

Before the first question, say:

`这几个比 HRV 更重要。我一次问一个，你直接回“有”或“没有”就行。`

Ask in this exact order:

1. `今天或最近跑步时有胸痛、胸闷吗？`
2. `有头晕、快晕倒、明显心悸吗？`
3. `最近 7-14 天有发热或病毒感染吗？`
4. `有已知心脏病、心律失常，或直系亲属早发猝死史吗？`

After each user answer:

- Treat `有` and `是` as positive answers.
- Treat `没有` and `否` as negative answers.
- If the answer is positive, stop the sequence and give a conservative result immediately.
- If the answer is negative, briefly acknowledge and ask the next question.
- If the answer is ambiguous, ask the same question again more clearly.

Use short acknowledgements only:

- After question 1 negative: `好，没有胸痛胸闷。下一题：有头晕、快晕倒、明显心悸吗？`
- After question 2 negative: `好，没有这类症状。下一题：最近 7-14 天有发热或病毒感染吗？`
- After question 3 negative: `好，没有近期发热或感染。最后一题：有已知心脏病、心律失常，或直系亲属早发猝死史吗？`

If question 4 is also negative:

- If current evidence is enough, give the final recommendation immediately.
- If current evidence is not enough, ask for resting heart rate trend first, then yesterday workout only if still needed.
- Do not ask for more data unless it will clearly change the recommendation bucket.

### If Any Red Flag Is Positive

Immediately output:

`结论：今天不建议跑。依据：你刚才提到 {red_flag_reason}，这类信号优先级高于恢复指标。建议：今天先别硬跑。提醒：这只是训练建议，不是医疗判断；如果有胸痛、晕厥、明显气短或心悸，请停止运动并尽快就医。`

Do not continue to resting heart rate or workout-load analysis.

### If The User Refuses Or Skips

`这些不是走流程，是拦风险。你不回答，我只能给更保守的建议。`

If they still refuse:

`结论：今天只建议轻松活动。依据：风险问题没有排清，我不会给更激进的建议。提醒：这只是训练建议，不是医疗判断。`

## Turn 4: Ask For Resting Heart Rate Or Yesterday Workout Only If Needed

Only do this if:

- All red flags are negative
- The recommendation is still uncertain
- HRV or sleep confidence was weak
- You need to decide between `轻松活动` and `轻松跑`, or between `轻松跑` and `正常跑`

Priority order:

1. Resting heart rate trend
2. Yesterday workout or training load

### Resting Heart Rate Prompt

`再补一张静息心率趋势图。最好带近 1 个月趋势和最近几天数据。`

Try to extract:

- Whether the latest resting heart rate is above, near, or below recent baseline
- Whether the latest few days are rising
- Whether dates are visible
- Confidence

Reduce into:

- `静息心率偏高`
- `静息心率接近常态`
- `静息心率偏低或正常`

### Yesterday Workout Prompt

`再补一张昨天运动记录或训练负荷图，我要看你是不是昨天已经把身体榨过一遍了。`

Try to extract:

- Whether the workout was easy, moderate, or hard
- Duration if visible
- Whether there was unusually high load
- Confidence

Reduce into:

- `昨天负荷高`
- `昨天负荷中等`
- `昨天负荷轻`

## Decision Policy

### Hard Stop First

Any of these means `今天不建议跑`:

- Chest pain or chest tightness during recent running
- Dizziness, near-fainting, or obvious palpitations
- Recent fever or viral illness
- Known heart disease or arrhythmia with current concern
- Strong cardiac family-history concern raised by the user
- The model sees an obvious abnormal alert in the screenshot and the user cannot clarify it

### Recovery Judgement

If red flags are all negative, judge recovery conservatively:

Strong signs against running:

- HRV clearly below recent baseline
- HRV trend worsening
- Sleep clearly insufficient or fragmented
- Resting heart rate above baseline
- Yesterday load clearly high

Map to outputs like this:

- Multiple strong negatives -> `今天只建议轻松活动`
- One or two moderate negatives -> `今天可以轻松跑`
- No red flags and recovery signals broadly stable -> `今天可以正常跑`

If confidence is weak, downgrade one level.

## Final Reply Format

Use exactly this structure:

- `结论：...`
- `依据：...`
- `建议：...`
- `提醒：仅供训练建议，不构成医疗建议；如有胸痛、晕厥、明显气短、心悸，请停止运动并就医。`

Examples:

`结论：今天只建议轻松活动。依据：HRV 心率变异性低于近期基线，昨晚睡眠不足，而且恢复趋势在变差。建议：如果非要动，走路或 20 分钟超轻松 jog 就够了。提醒：仅供训练建议，不构成医疗建议；如有胸痛、晕厥、明显气短、心悸，请停止运动并就医。`

`结论：今天可以轻松跑。依据：没有明显风险红旗，HRV 和睡眠都不算差，但恢复不够漂亮。建议：今天跑轻松配速，别碰强度。提醒：仅供训练建议，不构成医疗建议；如有胸痛、晕厥、明显气短、心悸，请停止运动并就医。`

## Failure Handling

### When The Image Is Weak

Say what is missing. Do not hallucinate specifics.

Good:

`我能看出最近几天偏低，但具体数值读不稳。`

Bad:

`你的 HRV 是 37ms，低了 12%。`

### When Inputs Conflict

`你给我的信息有点打架：{conflict}。这种情况我会按保守来。`

### When The User Wants A Faster Answer

`那我先按现在的信息给保守结论：{结论}。如果你愿意再补一张图，我可以把判断拉得更准一点。`

## What Not To Do

- Do not ask the user to choose which metric to send next
- Do not ask all 4 red-flag questions at once
- Do not turn the chat into a lecture
- Do not give numeric scores or fake precision
- Do not present this as medical clearance
- Do not ignore a positive red flag just because HRV or sleep looks good
