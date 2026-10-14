# Extracting architecturally significant requirements (ASRs)

*Artifact for Post #12.*

An ASR is a requirement that, if it changes, changes the architecture. Everything else is scope.

## Step 1 — The five filters

Run every requirement through these. Anything that trips a filter is a candidate.

| Filter | Trip condition | Example |
|---|---|---|
| **Quality** | It names a measurable property: latency, availability, throughput, recovery, retention | "Response within 3 seconds at peak" |
| **Scale** | It implies a volume, growth or concurrency figure | "25,000 applications a day, 5× on campaign days" |
| **Compliance** | It comes from a regulator, auditor, contract or law | "Payment data stored in-country" |
| **Integration** | It requires another party — internal or external — to change | "Partner fintechs submit applications via API" |
| **Change frequency** | It says how often something must be able to change | "New loan product live in 10 working days" |

## Step 2 — The unwritten ones

The most expensive ASRs are rarely in the document. Ask these six questions in every requirements workshop:

1. What must **never** happen, even during an outage? (Reveals fail-open vs fail-closed, and the real consistency requirement.)
2. What does the **regulator or auditor** ask for, and how often?
3. What happens to this data — and this decision record — in **8 years**?
4. Which **other teams or vendors** must change for this to work, and what is their release cadence?
5. What is the **peak**, not the average — and what event causes it?
6. What is the **cost** of the system being wrong for one hour? For one day?

## Step 3 — Make each ASR measurable

A requirement that cannot be measured cannot be designed for. Rewrite each candidate in this form:

> **When** \<stimulus\> **occurs in** \<environment\>, **the system will** \<response\> **within/with** \<measure\>.

*"The system must be fast"* becomes
*"When a customer submits a fund transfer during a salary-day peak (5× average load), the system will confirm or reject within 3 seconds at p99."*

## Step 4 — Record it

| Field | Content |
|---|---|
| ID | ASR-n |
| Requirement | The measurable statement |
| Source | Document, workshop, regulation, contract — and who owns it |
| Type | Quality / scale / compliance / integration / change frequency |
| Measure | The number, and how it will be tested |
| Architectural impact | What in the design exists *because of* this requirement |
| If it changes | What we would have to redesign |
| Confidence | High / medium / assumed — assumptions get an owner and a validation date |

## Step 5 — The discipline that makes this work

- Cap the list. **If you have more than 10 ASRs, you have a wish list.** Rank and cut.
- Every ASR gets a **named business owner** who can be asked to relax it. A requirement nobody will defend is not a requirement.
- Every "assumed" ASR gets a **validation date**. Assumptions that quietly become false are the standard cause of month-seven failures.
