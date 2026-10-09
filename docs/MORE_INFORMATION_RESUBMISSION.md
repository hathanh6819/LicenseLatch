# LicenseLatch V2 — response to steward request

Steward request: “App cannot establish real licensing authority or enforce permissions downstream.”

## Changes made

1. **Publisher self-declaration no longer activates a license.** `create_license` produces `AUTHORITY_PENDING`, not `ACTIVE`.
2. **Independent authority confirmation is mandatory.** Publisher and authority addresses must differ. Only the assigned authority wallet can call `confirm_license_authority`, and it must present the exact immutable attestation digest at the current epoch.
3. **Authority evidence is explicit and auditable.** Every proposal binds an HTTPS evidence URI and a `sha256:` attestation digest into the policy digest.
4. **Authority can withdraw the policy.** Both the publisher and assigned authority can deactivate it; stale epochs and requests bound to obsolete policy state fail closed.
5. **Permissions now cross a real contract boundary.** A compatible consensus result emits a finalized cross-contract call to a separately deployed `LicensedUseExecutor`.
6. **Downstream enforcement is implemented.** The executor accepts authorizations only from its configured LicenseLatch guard, binds each to a specific consumer and expiry, rejects forged/replayed authorizations, and permits exactly one successful consumption.
7. **Frontend matches the lifecycle.** Separate proposal and authority desks expose pending status, evidence URL/digest, assigned authority, executor, and consumer binding. Requests list only active policies.
8. **Adversarial tests cover the new guarantees.** Tests include unauthorized authority, wrong digest, inactive proposal, role collision, deterministic failure, semantic conflict, forged executor call, wrong consumer, receipt mismatch/replay, and successful one-time consumption.

## Honest boundary

LicenseLatch now establishes cryptographic protocol authority and enforceable downstream contract permissions. It still does not claim that a blockchain can independently prove copyright ownership or legal validity; reviewers can inspect the public evidence and the authority wallet’s attestation.

## Release gate

Do not resubmit using the old V1 address. Deploy both V2 contracts, execute the three-role live E2E, update `docs/LIVE_EVIDENCE.md` with explorer links and finalized readbacks, update the frontend environment, deploy it, and only then resubmit.
