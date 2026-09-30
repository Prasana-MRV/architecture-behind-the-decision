# Week 1 Friday challenge (Post #5)

## The brief

You have joined **Meridian Bank** as chief architect. Read [`../docs/meridian-bank-brief.md`](../../docs/meridian-bank-brief.md).

On day one the board tells you two things:
1. A digital-only competitor onboards a customer in under 5 minutes. Meridian takes 2 days.
2. The regulator wants evidence of resilience testing within 6 months.

**What is the first decision you make — and why that one first?**

Post your answer in the comments. Score it with [`reversibility-test.md`](reversibility-test.md) first.

## My answer

Not a technology choice. The first decision is: **which decisions belong to me, and which do not.**

Concretely, in week one I would decide and publish the **decision rights model**:

| Decision class | Score | Owner | Format |
|---|---|---|---|
| One-way doors: customer identity, data residency, core contracts, payment rails | 15–20 | Chief architect + accountable executive | ADR, with dissent recorded |
| Cross-team: service boundaries, integration style, shared platforms | 9–14 | Architecture group with the owning teams | One-page decision note |
| Everything else | 4–8 | The delivery team, no approval needed | Nothing |

Why this first, in one line: with 40 teams, 6 architects and two urgent mandates, the constraint is not knowledge — it is **decision throughput**. Every week spent approving component libraries is a week not spent on the onboarding journey or the untested failover.

The second decision is far less interesting and follows immediately: onboarding gets a dedicated team with an end-to-end owner, and the untested payments failover gets a date in the calendar with the regulator's letter attached to it.

**What I would deliberately *not* decide in week one:** the core modernisation strategy. It is the biggest one-way door in the estate, the evidence to decide it well does not exist yet, and a new architect deciding it in month one would be signalling confidence rather than exercising judgement.

### The best reader answers

- *"Freeze nothing, measure everything — you cannot decide anything credibly in month one without a baseline."* A fair challenge to the above. My counter: baselining is an action, not a decision, and it does not need my signature.
- *"Fix the two teams writing to the same customer table."* Correct that it matters, but it is a Q2 decision (score 14) that the teams can own once decision rights are clear.
