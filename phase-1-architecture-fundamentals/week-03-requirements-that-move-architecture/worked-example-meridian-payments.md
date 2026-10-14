# Worked example — Meridian payments: from 300 requirements to 9 ASRs

*Artifact for Post #15 (the Friday challenge) and Post #12.*

## The brief given to readers

Meridian is replacing the customer-facing layer of its payments hub.

- 4.2 million payment transactions a day, peaking at 5× on salary days.
- Instant payments must work 24×7; the market expects single-digit-second confirmation.
- Fraud scoring is currently synchronous on the payment path.
- Payment data must be stored in-country; audit trail retained 8 years.
- The mainframe core has a nightly batch window of 23:30–02:30.
- Partner fintechs want API access.
- The programme has a 12-month deadline and a fixed budget.

**Challenge: name the top five architecture drivers.**

## My answer — the ASRs that survive the filters

| ID | ASR (measurable) | Type | Architectural impact |
|---|---|---|---|
| ASR-1 | Confirm or reject an instant payment within **3 s at p99**, including fraud scoring, at 5× peak | Quality | Sets the end-to-end latency budget; forces a per-hop budget and decides where fraud scoring can sit |
| ASR-2 | Sustain the salary-day peak — **~21 million transactions/day, ~600 TPS in the peak hour, ~900 TPS burst** — with no manual intervention (see arithmetic below) | Scale | Decides partitioning, connection management and autoscaling signals; kills any design that serialises on a single core session |
| ASR-3 | Operate **24×7**, including during the 23:30–02:30 core batch window | Quality + constraint | The single most consequential driver: the customer-facing layer cannot depend on the core being available. Requires a store-and-forward / deferred posting design with reconciliation |
| ASR-4 | **No duplicate debits**, ever, including after retries, replays and failover | Quality (correctness) | Mandates idempotency keys on every financial event and a processed-events check in the same transaction as the ledger write (Week 26) |
| ASR-5 | Payment data **stored in-country**; 8-year reconstructable audit trail per transaction | Compliance | Decides region topology, backup location, vendor eligibility and log design (logs become evidence, not diagnostics) |
| ASR-6 | **Fail-open or fail-closed** on fraud-engine unavailability, decided per risk tier and approved by risk | Quality (availability vs risk) | Turns an operational accident into a designed, signed-off policy; drives circuit-breaker behaviour (Week 29) |
| ASR-7 | Partner APIs onboarded with **per-partner authorisation, rate limits and isolation** | Integration | Forces an edge design with per-partner quotas; prevents one partner exhausting shared capacity |
| ASR-8 | Recover the payments service with **RPO ≈ 0 and RTO ≤ 30 minutes**, demonstrated by a tested failover | Compliance + quality | Drives replication mode (synchronous for the ledger), DR pattern and a drill schedule with evidence for the regulator. Synchronous replication must stay in-country (ASR-5) and its round-trip comes out of the 400 ms ledger budget — which caps the distance between sites |
| ASR-9 | Support a **new payment rail or scheme change within 10 working days** | Change frequency | Pushes scheme-specific logic to adapters behind a stable internal contract |

## The top five, if forced to choose

**ASR-3, ASR-1, ASR-4, ASR-5, ASR-8.**

Reason: ASR-3 decides the *shape* of the architecture (decoupled from core availability). ASR-1 decides the *latency budget*. ASR-4 decides the *correctness model*. ASR-5 and ASR-8 decide the *topology* and are non-negotiable with the regulator.

ASR-2 is derived arithmetic, not a driver: once ASR-3 removes the core dependency, the volume is an engineering exercise.

## The arithmetic that made ASR-2 real

"21 million a day" is a number nobody can design against. Throughput is designed in transactions per second, at the peak, not the daily average.

| Step | Figure |
|---|---|
| Average day: 4.2 M ÷ 86,400 s | ≈ 49 TPS |
| Salary day at 5× | ≈ 21 M/day ≈ 243 TPS averaged over 24 h |
| Peak hour, assuming it carries ~10% of the day's volume | ≈ 2.1 M/h ≈ 583 TPS |
| Burst within the peak hour (×1.5) | ≈ 875 TPS |
| **Design point / load-test target** (≈ +30% headroom) | **≈ 900 TPS sustained, tested to 1,200 TPS** |

The "10% in the peak hour" figure is an **assumption**, recorded as such with an owner and a validation date (see the ASR template, step 5). It is the number most likely to be wrong, and the first to check against production telemetry.

## The arithmetic that made ASR-1 real

End-to-end budget of 3 s at p99, allocated per hop *before* any code is written:

| Hop | Budget (p99) |
|---|---|
| Mobile → edge (network, TLS, auth) | 400 ms |
| Edge → payment service | 100 ms |
| Limit and eligibility checks | 250 ms |
| Fraud scoring | 600 ms |
| Ledger write (synchronous, durable) | 400 ms |
| Scheme / rail call | 800 ms |
| Response path + client render | 450 ms |
| **Total** | **3,000 ms** |

A note on the maths: per-hop p99 budgets do not add up to an end-to-end p99 — hops rarely hit their tail on the same request, so the sum is deliberately conservative. Treat the table as a **design allocation** each team must meet, not a prediction. Validate end-to-end p99 with load tests at the ASR-2 design point.

Two consequences fall straight out of the table, and both are architecture decisions, not tuning:

1. Fraud scoring gets 600 ms. If the model needs 900 ms, it moves off the synchronous path for low-risk tiers — which requires ASR-6 to be agreed with risk first.
2. There is no room for a synchronous call to the mainframe core. That is ASR-3 restated in milliseconds, and it is what makes deferred posting and reconciliation unavoidable.

## What readers got right, and what most missed

- Nearly everyone named latency and volume. Those are the visible drivers.
- Fewer than a third named the **batch window** — the constraint that actually dictates the architecture.
- Almost nobody named **change frequency** (ASR-9), which is what decides whether the platform is still useful in year three.
