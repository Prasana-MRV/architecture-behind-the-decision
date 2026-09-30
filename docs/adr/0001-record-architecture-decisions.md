# ADR-0001: Record architecture decisions

- **Status:** Accepted
- **Date:** Week 1 of the series
- **Decision makers:** Series author, acting as chief architect for Meridian
- **Reversibility:** Two-way door

## Context

Across 52 weeks, roughly 60 significant decisions will be made about Meridian Bank's architecture. Readers will join at different weeks and need the earlier reasoning before they can judge a later choice.

More generally: in most estates, the most expensive question is "why did we do this?", asked three years late, after everyone who knew the answer has left.

## Options considered

### Option A — Explain decisions inside the posts only
- Gains: no extra work.
- Costs: reasoning scattered across 260 posts; unsearchable; no way to show supersession.

### Option B — A design document per phase
- Gains: a readable narrative.
- Costs: documents get edited, so the *original* reasoning disappears; rejected options vanish.

### Option C — Immutable ADRs, one per decision
- Gains: searchable, small, preserves rejected options and consequences, supports supersession, cheap enough to actually be done.
- Costs: discipline; the index must be maintained.

## Decision

We will record every significant Meridian decision as an immutable ADR in `docs/adr/`, using `adr-template.md`.

Because the value is not the document — it is the *rejected options* and the *consequences*, which no other format preserves.

## Consequences

**Positive**
- Any reader can reconstruct the reasoning behind the Week 52 reference architecture.
- Superseded decisions stay visible, which makes the evolution of the architecture teachable.

**Negative / accepted costs**
- About 30 minutes per decision.
- The index must be updated with each record, or it silently rots.

## What would make us revisit this

- If fewer than half the significant decisions are recorded by Week 13, the process is too heavy and should be simplified — not abandoned.

## References

- Michael Nygard, "Documenting Architecture Decisions" (2011).
