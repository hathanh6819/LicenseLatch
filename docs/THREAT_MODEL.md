# Threat model

| Threat | Control | Expected safe state |
|---|---|---|
| Requester invents favorable policy | Request binds an existing publisher-sealed digest | digest mismatch rejected |
| Publisher requests against own policy | role separation | request not created |
| Revenue/cap bypass | integer comparison before consensus | deterministic `REJECTED` |
| Sublicense or AI flag bypass | boolean rules before consensus | deterministic `REJECTED` |
| Prompt injection in policy/request | prompt marks all embedded instructions inert/hostile | bounded verdict only |
| Malformed/model failure | strict schema and enum checks | `CONSENSUS_UNRESOLVED` |
| Replay verdict | terminal request status | no second verdict/permission |
| Policy deactivated while pending | active policy rechecked at assessment | no positive transition |
| Wrong object evidence | policy and request digests stored in verdict | rejected binding mismatch |
| False legal/ownership claim | explicit scope note in contract/UI/docs | never asserted |
