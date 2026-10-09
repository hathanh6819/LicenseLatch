# LicenseLatch — Attested NFT Permission Gateway

LicenseLatch V2 turns an authority-confirmed NFT commercial-use policy into a consumer-bound downstream authorization. A publisher may propose terms, but the policy remains `AUTHORITY_PENDING` until a different authority wallet confirms the exact attestation digest. GenLayer consensus then compares an intended use with those immutable terms. A compatible result is finalized into a separate `LicensedUseExecutor`, where only the bound consumer can consume it, once, before expiry.

The previous V1 deployment remains historical evidence. V2 requires fresh deployments and fresh E2E evidence before resubmission.

## Claim boundary

The protocol proves which wallets proposed and independently attested a policy, which public evidence URI/digest they bound, and whether a downstream executor accepted and consumed a permission. It does **not** independently prove copyright ownership, legal validity of the evidence, or enforceability outside integrated contracts.

## V2 lifecycle

```text
publisher proposal -> AUTHORITY_PENDING
independent authority confirmation -> ACTIVE
requester submits consumer-bound use -> deterministic gate
GenLayer compatibility consensus -> finalized cross-contract dispatch
LicensedUseExecutor -> one-time consume by bound consumer
```

## Deployment order

The two contracts are intentionally circularly bound at configuration time, so deploy them in this order:

1. Deploy `contracts/license_latch.py` (no constructor arguments).
2. Deploy `contracts/licensed_use_executor.py` with the LicenseLatch address as `guard`.
3. When proposing a license, supply the executor address, an independent authority wallet, a public HTTPS authority-evidence URL, and its `sha256:` digest.

The LicenseLatch deployer receives no role. Publisher, authority, and requester/consumer roles come from the wallets that participate in each policy.

## Reviewer path

1. Connect any wallet and create a proposal on **Propose policy**.
2. Connect the assigned, different authority wallet on **Authority desk**, inspect the linked evidence, and confirm the digest.
3. Connect a third wallet on **Request a use**, select the active policy, and submit a consumer-bound request.
4. Run consensus review. A compatible result dispatches a finalized authorization to the configured executor.
5. In Studio or an integrating app, call `consume_authorization(permission_id, receipt)` from the exact consumer wallet. A second consume and any foreign wallet fail closed.

## Verification

```powershell
.\verify.ps1
```

Current local results: 16 contract/adversarial tests pass, including independent-authority gating, digest/epoch binding, deterministic failure, semantic conflict, finalized dispatch, downstream role enforcement, and replay prevention. The frontend production build also passes.

## Repository map

- `contracts/license_latch.py` — authority-gated policy and consensus coordinator
- `contracts/licensed_use_executor.py` — guarded, consumer-bound one-time executor
- `tests/` — lifecycle and adversarial coverage
- `frontend/` — proposal, authority, request, and ledger UI
- `docs/MORE_INFORMATION_RESUBMISSION.md` — point-by-point steward response
- `docs/LIVE_EVIDENCE.md` — update after V2 deployment and E2E
