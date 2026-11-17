# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one
# fixed plan to /output/entry.txt - the plan an AI agent would follow to turn
# $100, a computer with internet access and 30 days into the most money.
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so write no line end you do not mean to show. The program runs twice with
# no network, and both runs must write the same bytes.
#
# Why this plan: it sells one concrete, code-deliverable fix to buyers the
# agent finds by scanning for the flaw itself (so every prospect is already
# proven to need it), at a fixed price, with a free sample attached, a daily
# volume target, a kill rule for dead channels, a cash reserve that is never
# touched, and a second channel only once the first pays. No trading, no ads
# up front, no human labour, no luck.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Day 1: pick one fix an AI does better than a human - repairing broken product pages on small Shopify stores already taking orders.",
        "Build a scanner that finds stores with dead images, missing descriptions or slow pages, plus a one-page site and a $49 payment link.",
        "Days 2-3: fix three pages free for five stores and keep before/after screenshots as proof.",
        "Days 4-30: email 50 stores a day, each message naming its exact flaw and attaching the fixed page; charge $49 per store for the full fix, delivered by code the same day.",
        "Each fix is code, so a sale costs minutes, not hours.",
        "Target two sales a day ($98/day). Kill rule: any list under 1% replies after 200 emails is dropped; double the list that converts best.",
        "Spend $0 until $200 is banked, then try one second channel (Upwork) only if it beats email's dollars per hour.",
        "Keep the $100 as reserve; never spend on ads, trading or tools that do not pay back in 7 days.",
        "Expected: $1,200-$1,800 by day 30, from fixes, repeat work and referrals.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
