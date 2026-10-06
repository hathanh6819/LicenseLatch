# Verification

## Local gate

Run `./verify.ps1` from the repository root.

Coverage includes validation, immutable policy sealing, publisher authority, role separation, digest and epoch binding, deterministic rejection, compatible/incompatible/ambiguous semantic outcomes, malformed consensus, prompt injection, replay, and deactivation race safety.

## Live gate

Complete for programmatic SDK E2E on `0x67dFf8B0de804e414871F27baB1293fE189aeD9E`.

- Deployer is distinct from both ordinary test actors and has no protocol role.
- Happy request finalized `COMPATIBLE`, `APPROVED`, and issued one digest-bound permission.
- Revenue-cap and sublicensing conflicts were rejected deterministically without semantic verdicts.
- Disguised betting promotion finalized `INCOMPATIBLE` and issued no permission.
- Replay and unauthorized deactivation produced explicit errors with no protected-state mutation.
- Deactivation race rechecked policy state and prevented a pending request from becoming positive.
- Final readback: 2 licenses, 5 requests, 2 verdicts, 1 permission.

See [`LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md). Browser-wallet automation is not claimed.
