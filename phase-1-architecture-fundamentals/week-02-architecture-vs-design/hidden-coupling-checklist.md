# Finding couplings that are not in the diagram

*Artifact for Post #9 — anatomy of a hidden coupling.*

Architecture diagrams show intended dependencies. Outages come from the unintended ones. These are the seven places I look first.

| # | Hidden coupling | How to find it | Typical symptom |
|---|---|---|---|
| 1 | **Shared database tables** | Grep the data-access layers of every service for the same table names; check DB grants per application user | Two teams cannot release independently; schema change needs a change-advisory board |
| 2 | **Shared "common" libraries** | Look for a library imported by more than four services whose release notes include business changes | A version bump forces a coordinated release across teams |
| 3 | **Shared infrastructure with no quota** | One cluster, one connection pool, one message broker without per-tenant limits | A low-priority batch job degrades a customer journey |
| 4 | **Implicit ordering between jobs** | Read the scheduler, not the documentation | "It only fails when the file arrives late" |
| 5 | **Shared identity or certificate** | One service account or certificate used by multiple systems | One rotation takes down several systems at once |
| 6 | **Copy-pasted contracts** | Search for duplicated DTOs or event schemas across repos | A field changes meaning in one place and silently diverges |
| 7 | **Shared team** | Look at the delivery calendar, not the architecture | Two "independent" services always release together because the same four people build both |

## The measurement that settles arguments

Take the last 6 months of commits or change records. For each pair of services, count how often they changed **in the same week**.

High change-coupling with low architectural coupling means the boundary is wrong — regardless of what the diagram says.

## The rule

> If two services must be released together, they are one service with two deployments — and all the cost, none of the benefit.
