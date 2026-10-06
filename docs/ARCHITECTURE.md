# Architecture

## Proof obligation

LicenseLatch proves only that a request is compatible with the exact policy bytes sealed by a named publisher wallet. It does not prove NFT ownership, legal authority, copyright ownership, or enforceability.

## Distinct topology

```text
publisher wallet -> immutable license registry
requester wallet -> bound use-request registry
                      | deterministic bounds
                      v
                semantic compatibility consensus
                      |
           verdict registry -> permission record
```

This is not a revision/activation graph. Policies are immutable records. Requests are independent objects. Verdicts bind both digests. Only a compatible verdict creates a non-transferable protocol permission record.

## Authority table

| Claim | Authority/evidence | Enforcement |
|---|---|---|
| What this publisher permits | Exact policy bytes signed by publisher transaction | Immutable digest and publisher address |
| Declared intended use | Exact requester-authored request bytes | Request digest and requester address |
| Numeric/boolean compatibility | On-chain fields | Deterministic checks before AI |
| Semantic compatibility | Both bounded texts | GenLayer comparative consensus |
| Legal rights / NFT ownership | Not established | Explicitly outside claim boundary |

The deployer has no stored role. Any wallet can publish a policy; a distinct wallet can submit a request. Any wallet can trigger assessment because triggering consensus grants no discretionary power.
