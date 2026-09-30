# Meridian Bank — the running case

**Meridian Bank is fictional.** It is a composite built from patterns that recur across mid-sized banks: a mainframe core, a newer digital channel, an ambitious data programme and a regulator with a long memory. No real institution is described.

Every Friday challenge in the series is set at Meridian. By Week 52 the accumulated decisions form one complete reference architecture.

---

## 1. The business

| Attribute | Value |
|---|---|
| Type | Mid-sized retail and SME bank, single country, regulated |
| Customers | 8 million retail, 120,000 SME |
| Branches | 480, plus 2,100 ATMs |
| Channels | Mobile app (62% of transactions), internet banking, branch, call centre, partner APIs |
| Products | Savings, current accounts, term deposits, cards, personal loans, home loans, SME working capital |
| Technology staff | ~900, of which ~600 in delivery, spread across 40 teams |

## 2. The estate today

| System | Age | Notes |
|---|---|---|
| Core banking | 19 years | Vendor package on mainframe; heavily customised; nightly batch window 23:30–02:30 |
| Payments hub | 7 years | Instant payments, batch rails, standing instructions |
| Card management | 12 years | Vendor platform, quarterly release cycle |
| Digital channel | 4 years | Microservices on Kubernetes, cloud, weekly releases |
| Lending origination | 11 years | Monolith, ~2 million lines, 3 teams, release every 6 weeks |
| Data warehouse | 9 years | Nightly ETL from core; regulatory reporting depends on it |
| CRM | 5 years | SaaS, limited integration |
| Fraud engine | 3 years | Real-time scoring, called synchronously on the payment path |

## 3. Volumes

- Payments: 4.2 million transactions/day average; **peak 5× average** on salary days (last two and first two working days of the month) and during festival periods.
- Mobile app: 1.9 million daily active users; peak concurrency around 2% of DAU.
- Instant payments: market and regulator expect a response in **single-digit seconds, 24×7**.
- Card authorisations: 900,000/day.

## 4. Constraints

- **Regulatory:** payment data stored in-country; 8-year audit-trail retention; board-approved and *tested* business continuity plan; material outages reportable to the regulator.
- **Operational:** the mainframe batch window cannot be shortened before core modernisation completes (target: 3 years).
- **Financial:** technology budget grows 6% a year; cloud spend has grown 40% a year and is now under CFO scrutiny.
- **Organisational:** 40 delivery teams; 3 own the lending monolith; a central architecture group of 6; an SRE function of 11 covering the whole estate.

## 5. Strategic pressures

1. A digital-only competitor onboards customers in under 5 minutes. Meridian takes 2 days.
2. The board has approved an AI programme with no governance model yet.
3. The regulator has asked for evidence of resilience testing after a peer bank's 9-hour outage.
4. Fintech partners want API access that Meridian cannot currently offer safely.

## 6. Known pain

- Salary-day peaks push p99 fund-transfer latency above 4 seconds.
- The lending monolith cannot release independently of the digital channel.
- Two teams write to the same customer table from different services.
- Disaster recovery has never been tested with a full failover of the payments hub.
- "Active customer" has three different definitions in three different reports.

---

## Using this brief

Each Friday challenge quotes only the part of the brief it needs. Answers are published the following Monday; the significant ones become ADRs in [`adr/`](adr/).
