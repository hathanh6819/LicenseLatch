# Architecture V2

## Proof obligation

LicenseLatch proves a protocol authority chain: a publisher proposed exact policy bytes, a different assigned authority wallet confirmed an exact evidence digest, GenLayer reached a bounded compatibility verdict, and a guarded executor accepted a consumer-bound permission. Public evidence remains reviewer-verifiable; the protocol does not independently prove copyright ownership or legal validity.

```text
publisher -> pending policy + evidence digest
authority -> exact-digest confirmation -> active policy
requester -> intended use + bound consumer
              | deterministic gates
              v
          GenLayer consensus
              | finalized cross-contract message
              v
LicensedUseExecutor -> bound consumer -> one-time consumption
```

## Enforcement boundaries

| Claim | Authority/evidence | Enforcement |
|---|---|---|
| Proposed terms | Publisher transaction | Immutable policy digest |
| Authority consent | Distinct authority transaction | Exact attestation digest and epoch |
| Evidence reference | HTTPS URI + SHA-256 digest | Included in policy digest |
| Deterministic constraints | Structured on-chain fields | Rejected before AI |
| Semantic compatibility | Exact policy and request | Comparative consensus, strict schema |
| Downstream permission | Finalized guard-to-executor call | Consumer-bound, expiring, one-time consume |
| Copyright/legal ownership | External evidence and law | Explicitly not independently proven |

The deployer receives no stored role. Triggering assessment grants no discretionary authority. The executor rejects any caller other than its configured LicenseLatch guard, and authorization consumption rejects foreign wallets, receipt mismatches, expiry, and replay.
