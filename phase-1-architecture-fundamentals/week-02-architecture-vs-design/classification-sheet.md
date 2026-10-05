# Classification sheet: architecture or design?

*Artifact for Post #10 — the Friday challenge, with answers.*

Score each decision with the [reversibility test](../week-01-what-is-architecture/reversibility-test.md):
cost of change · blast radius · teams involved · time horizon, each 1–5. **4–8 = design · 9–14 = significant design · 15–20 = architecture.**

Show the per-axis scores, not just the total. In a review, the argument is almost always about one axis — usually time horizon — and the breakdown makes that argument visible.

## The ten decisions (challenge version)

1. Meridian's digital channel adopts a new logging library.
2. The customer identifier format used by the mobile app, the core and the data warehouse.
3. The lending team chooses a mocking framework for unit tests.
4. Payments moves fraud scoring from synchronous to asynchronous on the payment path.
5. The digital channel caches the product catalogue for 15 minutes.
6. Standardising on a single API style (REST) for all partner-facing interfaces.
7. The naming convention for Kubernetes namespaces.
8. Storing money as a decimal type with a fixed scale, everywhere.
9. The retry policy between the digital channel and the payments hub.
10. The lending monolith gets a new internal package structure.

---

## Answers

| # | Decision | Cost | Blast | Teams | Horizon | Total | Verdict | Why |
|---|---|---|---|---|---|---|---|---|
| 1 | Logging library | 1 | 1 | 1 | 1 | **4** | Design | One team, one release to change. *But:* if it defines the log format other systems parse, re-score — the format is the architecture, not the library. |
| 2 | Customer identifier format | 5 | 5 | 5 | 5 | **20** | **Architecture** | Every system, every channel, every report, forever. The definitive one-way door. Needs an ADR and a migration story before it is needed. |
| 3 | Mocking framework | 1 | 1 | 1 | 1 | **4** | Design | Invisible outside the team. If an architect is in this conversation, something is wrong. |
| 4 | Fraud scoring sync → async | 5 | 5 | 3 | 4 | **17** | **Architecture** | Changes the latency budget, the failure semantics (fail-open vs fail-closed), the customer-visible state and the regulator conversation. Not a tuning change. |
| 5 | 15-minute catalogue cache | 1 | 3 | 1 | 1 | **6** | Design | Reversible in one deploy — **unless** pricing or eligibility is served from it, in which case it becomes a consistency decision affecting money. Re-score then. |
| 6 | One API style for partners | 4 | 4 | 4 | 4 | **16** | **Architecture** | External contracts, partner tooling, multi-year commitments, many teams. Reversing it means asking every partner to re-integrate. |
| 7 | Namespace naming convention | 2 | 2 | 2 | 1 | **7** | Design (platform-wide) | Cheap to change early, annoying later. Decide once, in the platform team, and write it in the golden path — not in an ADR. |
| 8 | Money as fixed-scale decimal | 5 | 5 | 3 | 5 | **18** | **Architecture** | Data-type decisions on money propagate to every interface, ledger and report. Rounding disputes are found in reconciliation, years later. |
| 9 | Retry policy between two systems | 3 | 4 | 3 | 3 | **13** | Significant design | Two teams, one integration — but retry storms take down shared downstreams. Needs an agreed budget, not a committee. |
| 10 | Internal package structure of the monolith | 3 | 1 | 1 | 3 | **8** | Design → *watch it* | Internal today. The moment those packages become the extraction seams for decomposition, they are architecture (Week 12 — Modularity Before Microservices). |

## The pattern

Look at 2, 4, 6 and 8. None of them is a product, a framework or a diagram.

They are **identity, failure semantics, external contracts and data meaning** — the four categories that have been architecture in every estate I have worked in, whatever the technology of the decade.

## Re-scoring triggers

Keep a list. A design decision becomes architecture when:

- a second team starts depending on it;
- it crosses an organisational or contractual boundary;
- it starts serving money, identity or regulatory data;
- the cost of reversing it moves from a release to a migration.
