# LicenseLatch V2 — Live E2E Evidence

## Release identity

- Network: GenLayer Studio Dev (`chain_id 61997`)
- LicenseLatch V2: [`0xa567Db6130c0F595f7A919917B5Cc98F865a7604`](https://explorer-studio-dev.genlayer.com/address/0xa567Db6130c0F595f7A919917B5Cc98F865a7604)
- LicensedUseExecutor: [`0x5Ee91442bb33a3514A27dCb525aa3Bd841DF58f1`](https://explorer-studio-dev.genlayer.com/address/0x5Ee91442bb33a3514A27dCb525aa3Bd841DF58f1)
- Publisher wallet A: `0x1D283b45974B0be9630DFD1deC6A62a9B72B2760`
- Independent authority wallet B: `0xf96Cf822F9f4e76956AB9fAAa22B3BdCD7b10aD6`
- SDK-generated requester/consumer wallet C: `0xfe792d6Caa97D727fF32483ecc397F96C8Ddeaf8`
- Final state: 1 license, 3 requests, 2 verdicts, 1 permission, 1 consumed executor authorization
- Result: **PASS**

The deployment wallet is not a protocol actor. All three test roles are distinct. Fixture sources and their synthetic status are documented in [`TEST_RESOURCE_MANIFEST.md`](TEST_RESOURCE_MANIFEST.md).

## Finalized transaction trail

| # | Actor | Operation and verified readback | Explorer |
|---:|---|---|---|
| 1 | Publisher A | Propose policy; status `AUTHORITY_PENDING`, epoch 1 | [`0x03053a77…6b9408`](https://explorer-studio-dev.genlayer.com/transactions/0x03053a7789c2e29a271f5e92ff09d6f471876e925e0ff90e94b9c765106b9408) |
| 2 | Requester C | Unauthorized authority confirmation; policy remains pending | [`0x096ac971…f9ef5`](https://explorer-studio-dev.genlayer.com/transactions/0x096ac971a5f0f384d8062a06a8ebdb8534179fb7f3d69229ed9ef43f9bef9ef5) |
| 3 | Authority B | Confirm exact attestation; policy becomes `ACTIVE`, epoch 2 | [`0xb0fde6e3…520fe`](https://explorer-studio-dev.genlayer.com/transactions/0xb0fde6e31551f765128ff30a8e21ced5f4de5431c9e08a8df28dccfde61520fe) |
| 4 | Requester C | Submit compatible consumer-bound request | [`0x1c87ab9c…bc33b`](https://explorer-studio-dev.genlayer.com/transactions/0x1c87ab9c9e7aba9515d2323ce3393cc86475592c4b06f97a03c054e1963bc33b) |
| 5 | Publisher A | Consensus returns compatible; permission 1 queued for executor | [`0xe0d0fded…28bb3`](https://explorer-studio-dev.genlayer.com/transactions/0xe0d0fded078fe1cb80a302e9bde1cede18137d1cae6793ecad39b9bc9e128bb3) |
| 6 | Authority B | Foreign consumer attempt rejected; authorization remains `ACTIVE` | [`0xad852afe…0b321`](https://explorer-studio-dev.genlayer.com/transactions/0xad852afea04cba142c6402503fbc49be8dee9b9618dc102bd756cea1b040b321) |
| 7 | Consumer C | Bound consumer consumes permission; executor becomes `CONSUMED` | [`0x2d8c862d…e9ab3`](https://explorer-studio-dev.genlayer.com/transactions/0x2d8c862d6b2726039b841c54fa95f784b4513530a3bf4b9f01fe965fbb6e9ab3) |
| 8 | Consumer C | Replay consume rejected; state remains `CONSUMED` | [`0xce794754…b5b50`](https://explorer-studio-dev.genlayer.com/transactions/0xce794754a64a45f23daa9935eff67e23ae2ab6d9ffd4bb11c502ba032c2b5b50) |
| 9 | Requester C | Revenue exceeds cap; deterministic `REVENUE_CAP_EXCEEDED` | [`0x3a338213…78a17`](https://explorer-studio-dev.genlayer.com/transactions/0x3a338213001463dbc66a3498e4ca52676c5357a65559cb8aba45d51d4a378a17) |
| 10 | Requester C | Submit disguised betting-platform use | [`0xe40ad8ce…979bd`](https://explorer-studio-dev.genlayer.com/transactions/0xe40ad8ce7eee98ff7fdcea1efb5a2a6e7aa3c881517d99c889768367be4979bd) |
| 11 | Authority B | Semantic review rejects conflict; no second permission | [`0x39cb4654…5242f`](https://explorer-studio-dev.genlayer.com/transactions/0x39cb46546033191e6bed41a59ec78fbfee2a91b8944ae397a8a7a579a0f25242f) |

## Critical finalized readbacks

- Main protocol: version `2`, independent wallet attestation, finalized cross-contract authorization.
- Executor guard: `0xa567db6130c0f595f7a919917b5cc98f865a7604`.
- Permission 1 binds consumer `0xfe792d6caa97d727ff32483ecc397f96c8ddeaf8` and executor `0x5ee91442bb33a3514a27dcb525aa3bd841df58f1`.
- Executor authorization 1 reached `ACTIVE`, rejected a foreign caller, then reached `CONSUMED` from the bound consumer.
- Replay preserved `CONSUMED`; it did not create another authorization.
- Adversarial betting request ended `REJECTED`; final permission count stayed 1.

## Reproduce

```powershell
node scripts/create_test_wallet.mjs
node scripts/run_live_e2e.mjs 0xa567Db6130c0F595f7A919917B5Cc98F865a7604 0x5Ee91442bb33a3514A27dCb525aa3Bd841DF58f1
```

The runner prompts invisibly for publisher and authority keys and reads the SDK-generated requester key from a Git-ignored local file.
