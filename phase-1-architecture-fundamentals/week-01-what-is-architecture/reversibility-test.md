# The reversibility test

*Artifact for Post #2 — "The 4-question test I use to decide whether something is architectural."*

The point is not to produce a number. It is to stop two failures that cost real money:

- treating a reversible decision as a formal one — and spending six weeks in review on something a team could have tried in two days;
- treating an irreversible decision as routine — and discovering in year three that it constrains everything.

## The four questions

| # | Question | 1 point | 3 points | 5 points |
|---|---|---|---|---|
| 1 | **Cost of change.** If we are wrong, what does reversing it cost? | Hours or days, one team | Weeks, a few teams | Months, a programme, or a contract |
| 2 | **Blast radius.** How much of the estate does it touch? | One module | One system or journey | Multiple systems, partners or channels |
| 3 | **Coupling to others.** How many teams must agree or change with us? | None | 2–4 teams | 5+ teams, or external parties |
| 4 | **Time horizon.** How long will we live with it? | Until the next release | 1–2 years | 5+ years, or the life of a contract |

Score each question **1 to 5**. The 1 / 3 / 5 columns are anchors; use 2 or 4 when a decision genuinely sits between them. Totals run from 4 to 20.

**Score 4–8** — Design decision. Let the owning team decide and move on.
**Score 9–14** — Significant design decision. One page, two reviewers, no ceremony.
**Score 15–20** — Architecture decision. Write an ADR. Name the options and the dissent. Get the right people in one room, once, with the pre-work done.

## What the score does *not* mean

A high score does not mean "go slowly on everything". It means: this is where the analysis budget goes. Most estates spend it evenly, which is the same as spending it badly.

## Worked examples (Meridian Bank)

| Decision | Q1 | Q2 | Q3 | Q4 | Total | Verdict |
|---|---|---|---|---|---|---|
| Customer identifier format used across channels and the core | 5 | 5 | 5 | 5 | **20** | Architecture. One-way door. ADR, plus a migration plan before it is needed. |
| Buy vs build the lending origination engine | 5 | 5 | 3 | 5 | **18** | Architecture. The full decision record arrives in Week 6. |
| Making the fraud check synchronous on the payment path | 3 | 5 | 3 | 5 | **16** | Architecture. Decides the latency budget and the fail-open/fail-closed policy for the whole bank. |
| Choosing the message key for the transaction event stream | 3 | 3 | 3 | 5 | **14** | Significant design. Repartitioning later is painful but possible — document the key choice. |
| Adopting a new UI component library in the mobile app | 1 | 1 | 1 | 1 | **4** | Design. Team decides. |
| Adding a cache in front of the product catalogue | 1 | 3 | 1 | 1 | **6** | Design — *unless* it becomes the source of truth for pricing, at which point re-score it. |

## The one-line version

> **If we're wrong about this, what does it cost to change our mind?**

Low cost: let the team decide and move fast.
High cost: slow down, write it down, and get the right people in the room.

## How to use it in a review

1. Score the decision **before** discussing the options. The score sets the format of the discussion, not the outcome.
2. Re-score anything that changes category — a design decision can become architecture when volumes, partners or regulation change (see the cache example above).
3. Keep the scores. A year later they tell you whether your instinct about reversibility was calibrated.
