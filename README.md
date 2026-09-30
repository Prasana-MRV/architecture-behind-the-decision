# Architecture Behind the Decision

A public, year-long record of architecture **decisions** — the context, the options, the trade-offs, the failures and the outcomes.

This repository is the companion to the LinkedIn series *Architecture Behind the Decision*:
**52 weeks · 5 posts per week · Post #1 to Post #260.**

> Architecture is the set of decisions that are expensive to change.
> This repo is where those decisions are written down.

---

## Why this repo exists

LinkedIn posts disappear in a scroll. Decisions shouldn't.

Every week of the series produces one artifact — a decision record, a template, a checklist, a calculator or a diagram — that you can copy into your own organisation and use on Monday morning.

Everything here is **generic and anonymised**. No client, employer, vendor or production system is identified. Scenarios are composites built from patterns common across enterprise and BFSI estates.

---

## The weekly formula

| Day | Format | Job of the post |
|---|---|---|
| Monday | THINK | Take a position; reframe a concept |
| Tuesday | DECODE | Explain how and why, at practitioner depth |
| Wednesday | DECIDE | Show a real trade-off and the decision logic |
| Thursday | BREAK | Tell a failure story: timeline, cause, fix, lesson |
| Friday | DESIGN | Pose a challenge at Meridian Bank; review answers |

**Signature framework:**
`Problem → Context → Requirements → Constraints → Options → Trade-offs → Decision → Failure → Outcome`

---

## Meridian Bank

Every Friday challenge is set at **Meridian Bank** — a fictional, composite mid-sized bank used as the running case for the whole year.

Read the brief first: [`docs/meridian-bank-brief.md`](docs/meridian-bank-brief.md)

---

## Repository map

```
docs/
  meridian-bank-brief.md          The running case for all 52 weeks
  adr/                            Architecture Decision Records
    README.md                     How ADRs are used here, and the index
    adr-template.md               The template to copy
    0001-record-architecture-decisions.md
phase-1-architecture-fundamentals/  Weeks 1–6, Posts #1–#30
  README.md                       Phase overview and index
  week-01-what-is-architecture/   Reversibility test, whiteboard-breaking exercise, first Meridian challenge
tools/
  decision_cost.py                Reversibility / blast-radius scoring
  check_links.py                  Verifies every relative link in the repo (run in CI)
```

A new week's folder is added as each week of the series is published.

---

## What's in the repo

### [Phase 1 — Architecture Fundamentals](phase-1-architecture-fundamentals/README.md) (Weeks 1–6, Posts #1–#30)

| Week | Theme | Artifacts | ADR |
|---|---|---|---|
| 01 | Architecture Is the Decisions That Hurt to Change | Reversibility test, whiteboard-breaking exercise, ADR template, Meridian brief | [0001](docs/adr/0001-record-architecture-decisions.md) |

Next: **Week 2 — Where Architecture Ends and Design Begins.**

---

## Using the tools

Python 3.8+, standard library only.

```bash
python tools/decision_cost.py --scores 5 5 3 4
python tools/check_links.py
```

---

## How to use this repo

- **Architects:** copy the templates. They are deliberately short — a template nobody fills in is worth nothing.
- **Engineers preparing for architecture roles:** work the Friday challenges before reading the answers in `docs/adr/`.
- **Teams:** run a week per fortnight as an internal session. Each week's README ends with discussion questions.

Disagreement is welcome. Open a **Challenge a decision** issue with your reasoning (see [`CONTRIBUTING.md`](CONTRIBUTING.md)). A better argument does not edit an ADR — it produces a new one that supersedes it.

---

## License

Content: **CC BY 4.0** — use it, adapt it, credit it.
Code in `tools/`: **MIT**.
