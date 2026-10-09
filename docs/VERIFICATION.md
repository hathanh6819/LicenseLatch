# Verification

## Local release gate

Run `./verify.ps1` from the repository root. It executes 16 contract/adversarial tests, GenVM lint on both contracts, 4 frontend state tests, TypeScript checking, and a production Vite build.

Coverage includes independent authority activation, evidence-digest and epoch binding, role separation, deterministic rejection, semantic outcomes, malformed consensus, prompt injection, cross-contract dispatch, forged executor calls, wrong consumers, expiry, and replay.

## Live release gate

Complete on LicenseLatch V2 `0xa567Db6130c0F595f7A919917B5Cc98F865a7604` and executor `0x5Ee91442bb33a3514A27dCb525aa3Bd841DF58f1`.

- Publisher, authority, and requester/consumer are three distinct wallets; the deployment wallet has no protocol role.
- Unauthorized attestation left the policy pending; the assigned authority activated the exact digest at epoch 2.
- Compatible consensus issued one consumer-bound permission and finalized delivery to the executor.
- A foreign consumer was rejected; the bound consumer succeeded once; replay preserved `CONSUMED`.
- Revenue-cap failure was deterministic and issued no verdict or permission.
- Disguised betting promotion finalized `REJECTED` and issued no additional permission.
- Final readback: 1 license, 3 requests, 2 verdicts, 1 permission, 1 consumed authorization.

See [`LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md) for all explorer links and readbacks.
