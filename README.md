# ai-judge-rich-01

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/cheoriin17-lang/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/cheoriin17-lang/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Entry for make.fun competition `ai-judge-rich-01` ("Make the AI judge rich"):
a deterministic Python 3.13 program (standard library only, no network)
that writes one 30-day plan to `/output/entry.txt` — the plan an AI agent
starting with $100, a computer with internet access and 30 days would
follow to end with the most money. The plan sells one concrete,
code-deliverable fix (repairing broken product pages on small Shopify
stores) to buyers the agent finds by scanning for the flaw itself, at a
fixed $49 price, with a free sample attached, a daily volume target, a
kill rule for dead channels, and a cash reserve that is never touched.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt`: 996 UTF-8 characters, identical on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9etrdpz6&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
