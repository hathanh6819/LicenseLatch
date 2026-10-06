# Live E2E Evidence

## Release identity

- Network: GenLayer Studio Next (`chain_id 61997`)
- Contract: [`0x67dFf8B0de804e414871F27baB1293fE189aeD9E`](https://explorer-studio-dev.genlayer.com/address/0x67dFf8B0de804e414871F27baB1293fE189aeD9E)
- Production frontend: [license-latch-frontend.thanhha68199.workers.dev](https://license-latch-frontend.thanhha68199.workers.dev)
- Deployment transaction: [`0x42ee3786...0592d`](https://explorer-studio-dev.genlayer.com/transactions/0x42ee3786a6f180407de50a4ff8e833f655ecd3c127426e072c841df0e770592d)
- Policy publisher/test wallet A: `0x1D283b45974B0be9630DFD1deC6A62a9B72B2760`
- Use requester/test wallet B: `0xf96Cf822F9f4e76956AB9fAAa22B3BdCD7b10aD6`
- Date: 2026-10-06

The deployer address is distinct from both test actors and receives no protocol role. Reviewers can repeat the journey with their own two wallets and independent records.

## Finalized transaction trail

| # | Actor | Operation and verified outcome | Explorer |
|---:|---|---|---|
| 1 | Wallet A | Seal primary policy; license 1 becomes `ACTIVE` | [`0xf0932d1d...28f61`](https://explorer-studio-dev.genlayer.com/transactions/0xf0932d1d44607b96960ef4260ffeb0dd845cdf8340d254609fa2e32855728f61) |
| 2 | Wallet B | Submit compatible apparel use; request 1 becomes `SEMANTIC_PENDING` | [`0x4be66fdf...cd758`](https://explorer-studio-dev.genlayer.com/transactions/0x4be66fdf8f738588ee50273e23286ea594fac4e90a241560a22953af50fcd758) |
| 3 | Wallet A | Assess compatible use; `COMPATIBLE`, request `APPROVED`, permission 1 issued | [`0x56d18124...fc3bd`](https://explorer-studio-dev.genlayer.com/transactions/0x56d1812466ffea2118c2704ea488374c49ac38054572160b7cc28384162fc3bd) |
| 4 | Wallet B | Replay assessment rejected with `REQUEST_NOT_ASSESSABLE`; no mutation | [`0x94dba003...cfa764`](https://explorer-studio-dev.genlayer.com/transactions/0x94dba003edcbb0b553f34f5c5924e2e7a02c467a32d36b9025d2c1ed2acfa764) |
| 5 | Wallet B | Revenue 30,000 exceeds 25,000 cap; deterministic `REJECTED`, no AI verdict | [`0x148285fa...b9fb87`](https://explorer-studio-dev.genlayer.com/transactions/0x148285fa3e09e26f3b265fbd9ccb1c512a50be560cffa0c8e033a366d9b9fb87) |
| 6 | Wallet B | Sublicensing requested against prohibition; deterministic `REJECTED` | [`0x1d9bd04c...1457d5`](https://explorer-studio-dev.genlayer.com/transactions/0x1d9bd04ca1ce2ba7b2187c7d684dca6ae940a72ce799ee033446f46b841457d5) |
| 7 | Wallet B | Submit disguised betting-platform campaign | [`0x9ea336f7...71f62`](https://explorer-studio-dev.genlayer.com/transactions/0x9ea336f729bc673d8d577605f57101364faeecfa8bba676a2e40840aa0471f62) |
| 8 | Wallet A | Semantic assessment returns `INCOMPATIBLE` with industry/purpose conflict; no permission | [`0x7265ecfd...3bc22`](https://explorer-studio-dev.genlayer.com/transactions/0x7265ecfd627b96c58e98f74422ea4553d50b3cd2b2bbe3b4ca672ca04ab3bc22) |
| 9 | Wallet A | Seal second policy for deactivation-race test | [`0x1668d843...6d55d`](https://explorer-studio-dev.genlayer.com/transactions/0x1668d84374053b7d416772a86966559d12f1c4714dc175d548b74cc08d96d55d) |
| 10 | Wallet B | Submit request 5 while second policy is active | [`0x12b204a6...d0270`](https://explorer-studio-dev.genlayer.com/transactions/0x12b204a6cd9d7f78b59f28a317b724b79ddd36f0dc81abf0514584b0f96d0270) |
| 11 | Wallet B | Unauthorized deactivation rejected with `ONLY_LICENSE_PUBLISHER`; policy unchanged | [`0x0c575d01...cadcd`](https://explorer-studio-dev.genlayer.com/transactions/0x0c575d014282cb9c2ee5263b453c454855054c24b575b7bf8973c2efd36cadcd) |
| 12 | Wallet A | Publisher deactivates second policy; status `INACTIVE`, epoch 2 | [`0xd7f95d0e...6e694`](https://explorer-studio-dev.genlayer.com/transactions/0xd7f95d0e6b640e499e77eaa687babdc43dfe1b0ed201de34b8237b2fb9c6e694) |
| 13 | Wallet B | Pending assessment rejected with `LICENSE_NOT_ACTIVE`; no verdict/permission created | [`0xe4ced720...8197a`](https://explorer-studio-dev.genlayer.com/transactions/0xe4ced720d4925ea54d708a1d038d6238721d5067904717aed495bbde0a28197a) |

## Final readback

`get_counts()` returned `2 licenses / 5 requests / 2 verdicts / 1 permission`.

- License 1 remains `ACTIVE`; request 1 is `APPROVED` with verdict `COMPATIBLE` and permission 1 bound to both policy and request digests.
- Requests 2 and 3 are deterministically `REJECTED` for revenue-cap and sublicensing violations and created no semantic verdict.
- Request 4 is `REJECTED`; verdict 2 is `INCOMPATIBLE` with `INDUSTRY_RESTRICTION` and `PURPOSE_MISMATCH`.
- License 2 is `INACTIVE`, epoch 2. Its pre-existing request 5 remains `SEMANTIC_PENDING`; assessment after deactivation created no positive state.
- Replay and unauthorized operations finalized with explicit safe errors and did not mutate protected state.

Programmatic SDK E2E result: **PASS**. Browser-wallet automation is not claimed. All policy and use fixtures are synthetic and their limitations are documented in `TEST_RESOURCE_MANIFEST.md`.
