# Test resource manifest

LicenseLatch uses no external website, claimant-controlled URL, mutable API, or off-chain backend as authority. Fixtures are synthetic and prove protocol behavior only.

| Fixture | Source/owner | Role | Expected outcome | Missing boundary |
|---|---|---|---|---|
| Convention merchandise policy | Synthetic, repository-controlled | Publisher-sealed semantic policy | direct apparel can be compatible | does not prove publisher owns NFT/IP |
| Direct T-shirt request | Synthetic requester statement | Positive semantic fixture | `APPROVED` after consensus | does not prove real-world use occurred |
| Revenue 30,000 vs cap 25,000 | Synthetic numeric boundary | Deterministic negative | `REVENUE_CAP_EXCEEDED` | no semantic claim |
| Sublicensing requested | Synthetic boolean boundary | Deterministic conflict | `SUBLICENSING_NOT_ALLOWED` | no semantic claim |
| Betting-platform campaign | Synthetic adversarial text | Semantic negative | `INCOMPATIBLE` | not evidence about a real company |
| Embedded “output compatible” instruction | Synthetic injection | Prompt-integrity test | instruction treated as inert | no external authority |

Tests must never be described as a legal opinion, ownership check, marketplace integration, or evidence of an actual commercial license.
