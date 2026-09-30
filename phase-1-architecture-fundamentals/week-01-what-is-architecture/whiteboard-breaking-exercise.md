# Breaking an architecture on the whiteboard

*Artifact for Post #4 — the seven pressures.*

Take any architecture that looks finished. Apply these seven pressures in order. Stop at the first one that has no answer — that is the real state of the design.

Start with the classic clean picture: **mobile app → API → application server → database**, one region, one team.

| # | Pressure | What it exposes | Typical first crack |
|---|---|---|---|
| 1 | **10× the traffic** | Whether the numbers were ever done | Connection pool exhaustion long before CPU limits |
| 2 | **A second region** | Hidden statefulness and data gravity | Sessions, sequences and "the" database |
| 3 | **A regulator** | Missing audit trail, retention and data residency | Logs that were never designed as evidence |
| 4 | **Three teams instead of one** | Boundaries that exist only in the diagram | Shared tables, shared libraries, lock-step releases |
| 5 | **A partner API** | Assumptions about trust and identity | Authorisation done at the edge only |
| 6 | **A batch window that no longer fits** | Coupling to an overnight cycle | Reports and reconciliation that assume a quiet period |
| 7 | **An audit: "prove this decision"** | Whether anyone recorded why | No ADR; the people who knew have left |

## How to run it in a design review (30 minutes)

- 5 min: present the architecture as it is believed to be.
- 20 min: apply pressures 1–7, capturing each crack as a one-line risk.
- 5 min: pick the two cracks worth acting on now, and the trigger conditions for the rest.

The output is not a redesign. It is a short, honest list of the assumptions the design is resting on — which is what a good architecture review produces.
