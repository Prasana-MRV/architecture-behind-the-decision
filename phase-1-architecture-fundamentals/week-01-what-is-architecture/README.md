# Week 1 — Architecture Is the Decisions That Hurt to Change

**Posts #1–#5 · Phase 1: Architecture Fundamentals**

> **Thesis:** Architecture is not the diagram. It is the small set of decisions that are expensive to reverse — and knowing which ones those are.

## Posts this week

| # | Day | Format | Post |
|---|---|---|---|
| 1 | Mon | THINK | Twenty years in, my definition of architecture fits in one line |
| 2 | Tue | DECODE | The 4-question test I use to decide whether something is "architectural" |
| 3 | Wed | DECIDE | There is no perfect architecture — only the least-wrong one for this context |
| 4 | Thu | BREAK | I broke a clean three-tier architecture on a whiteboard in seven steps |
| 5 | Fri | DESIGN | You are the architect for Meridian Bank. What is the first decision you make? |

## Artifacts in this folder

- [`reversibility-test.md`](reversibility-test.md) — the four-question test, with scoring and worked examples
- [`whiteboard-breaking-exercise.md`](whiteboard-breaking-exercise.md) — the seven pressures used in Post #4, as a reusable design-review exercise
- [`friday-challenge.md`](friday-challenge.md) — the Week 1 challenge and my answer

Tool: [`../tools/decision_cost.py`](../../tools/decision_cost.py) — scores a decision on the four questions from the command line.

Also introduced this week: [`../docs/adr/adr-template.md`](../../docs/adr/adr-template.md) and [`../docs/meridian-bank-brief.md`](../../docs/meridian-bank-brief.md).

## Study references

- Mark Richards & Neal Ford, *Fundamentals of Software Architecture*, ch. 1–2
- Martin Fowler, "Who Needs an Architect?", IEEE Software (2003)
- Michael Nygard, "Documenting Architecture Decisions" (2011)

## Discussion questions for a team session

1. List the five decisions in your current system that would be hardest to reverse. Who made them, and when?
2. Which of them were ever written down?
3. How many of your last ten "architecture" meetings were about decisions that were actually cheap to change?
