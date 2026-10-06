# LicenseLatch — NFT Commercial Use Permission Gate

LicenseLatch determines whether a proposed NFT use is compatible with an immutable commercial-use policy sealed by a publisher wallet. Deterministic code checks revenue, expiry, sublicensing and AI-training constraints; GenLayer validators handle only the bounded semantic comparison.

**Live contract:** [`0x67dFf8B0de804e414871F27baB1293fE189aeD9E`](https://explorer-studio-dev.genlayer.com/address/0x67dFf8B0de804e414871F27baB1293fE189aeD9E) on GenLayer Studio Next. The finalized two-wallet transaction trail is in [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).

## Claim boundary

An `APPROVED` record means only “compatible with the exact publisher-sealed policy inside LicenseLatch.” It is not proof of NFT ownership, copyright ownership, legal authority, enforceability, or real-world compliance.

## Why GenLayer

Code can compare caps and flags, but cannot reliably decide whether a “lifestyle rewards campaign” is actually prohibited gambling promotion. Validators compare the exact sealed policy and exact request. The contract strictly validates the structured verdict and creates a permission record only for `COMPATIBLE` consensus.

## Architecture

```text
immutable policy -> bound request -> deterministic gate
                                   -> semantic verdict -> permission record
```

There is no owner, constructor role, custody, admin allowlist, mutable policy, backend authority, or model-controlled transfer. The deployer receives no protocol capability. Any reviewer can use their own wallet to publish a separate policy and a distinct wallet to request a use.

## Reviewer path

1. Deploy `contracts/license_latch.py` with no constructor inputs.
2. Open License Library and connect any Studio Next wallet.
3. Publish a policy; the UI creates a certificate card automatically.
4. Connect a different wallet, select the card, and submit a bounded use request.
5. Run compatibility review. A compatible request produces `AUTHORIZED`; prohibited use produces `OUTSIDE LICENSE`.
6. Inspect Decision Ledger for deterministic failures and semantic verdicts. No manual record IDs are required.

## Verification

```powershell
.\verify.ps1
```

Current local results:

- Contract/adversarial tests: 21 passed
- GenVM lint: 3 checks passed
- Frontend state tests: 3 passed
- TypeScript/Vite production build: passed

Live SDK E2E passed with 2 licenses, 5 requests, 2 semantic verdicts, and 1 permission. It covers compatible authorization, two deterministic failures, adversarial semantic conflict, replay, unauthorized deactivation, and deactivation-race safety. Browser-wallet automation is not claimed.

## Repository map

- `contracts/license_latch.py` — deployable contract
- `tests/` — lifecycle, binding and adversarial tests
- `frontend/` — responsive licensing-desk client
- `scripts/run_live_e2e.mjs` — hidden-key two-wallet live runner
- `docs/ARCHITECTURE.md` — proof and authority boundaries
- `docs/TEST_RESOURCE_MANIFEST.md` — exact synthetic fixture provenance
- `docs/THREAT_MODEL.md` — attacks and safe failure states
- `docs/VERIFICATION.md` — local/live release gates
- `docs/LIVE_EVIDENCE.md` — finalized deployment, transaction trail, and readbacks
