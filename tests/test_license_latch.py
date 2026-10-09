from conftest import *
def test_empty_protocol(runtime):
 _,c,_,_,_,_=runtime;assert c.get_counts()=={"licenses":0,"requests":0,"verdicts":0,"permissions":0};assert c.get_protocol()["version"]==2
def test_policy_waits_for_independent_authority(runtime):
 _,c,g,_,_,_=runtime;assert license(c)==1;x=c.get_license(1);assert x["status"]=="AUTHORITY_PENDING";sender(g,REQUESTER);assert c.confirm_license_authority(1,1,ATTESTATION)=="ONLY_INDEPENDENT_AUTHORITY"
def test_authority_digest_and_epoch_are_bound(runtime):
 _,c,g,_,_,_=runtime;license(c);sender(g,AUTHORITY);assert c.confirm_license_authority(1,1,"sha256:"+"0"*64)=="ATTESTATION_DIGEST_MISMATCH";assert c.confirm_license_authority(1,1,ATTESTATION)=="ACTIVE";assert c.get_license(1)["epoch"]==2
def test_pending_policy_cannot_accept_requests(runtime):
 _,c,g,_,_,_=runtime;license(c);x=c.get_license(1);sender(g,REQUESTER);assert c.submit_use_request(1,x["policy_digest"],USE,"Apparel","Worldwide",1,False,False,"Enough evidence note",REQUESTER,1)=="LICENSE_NOT_ACTIVE"
def test_invalid_authority_is_rejected(runtime):
 _,c,_,_,_,_=runtime;assert c.create_license("Valid name","0x"+"a"*40,"All",POLICY,1,2000000000,False,False,PUBLISHER,ATTESTATION,"https://evidence.example",EXECUTOR)=="INVALID_INDEPENDENT_AUTHORITY"
def test_authority_can_deactivate(runtime):
 _,c,g,_,_,_=runtime;activate(c,g);assert c.deactivate_license(1,2)=="INACTIVE"
def test_role_separation(runtime):
 _,c,g,_,_,_=runtime;activate(c,g);x=c.get_license(1);assert c.submit_use_request(1,x["policy_digest"],USE,"Apparel","Worldwide",1,False,False,"Enough evidence note",AUTHORITY,2)=="ROLE_SEPARATION_REQUIRED"
def test_happy_request_pending(runtime):
 _,c,g,_,_,_=runtime;assert request(c,g)==1;assert c.get_use_request(1)["status"]=="SEMANTIC_PENDING"
def test_deterministic_failure(runtime):
 _,c,g,n,_,_=runtime;request(c,g,expected_revenue=30000);assert c.get_use_request(1)["deterministic_reason"]=="REVENUE_CAP_EXCEEDED" and not n.prompts
def test_compatible_dispatches_bound_authorization(runtime):
 _,c,g,n,_,calls=runtime;request(c,g);r=c.get_use_request(1);sender(g,OUTSIDER);assert c.assess_use_request(1,r["request_digest"])==1;p=c.get_permission(1);assert p["consumer"]==REQUESTER and p["executor"]==EXECUTOR and p["status"]=="AUTHORIZATION_QUEUED";assert len(calls)==1;assert "authority-confirmed" in n.prompts[0]
def test_incompatible_has_no_permission(runtime):
 _,c,g,n,_,calls=runtime;request(c,g);n.answer={"decision":"INCOMPATIBLE","reasons":["INDUSTRY_RESTRICTION"],"explanation":"The proposed gambling campaign conflicts with policy."};r=c.get_use_request(1);c.assess_use_request(1,r["request_digest"]);assert c.get_counts()["permissions"]==0 and not calls
def test_conflicting_model_fails_closed(runtime):
 _,c,g,n,_,calls=runtime;request(c,g);n.answer={"decision":"COMPATIBLE","reasons":["PURPOSE_MISMATCH"],"explanation":"Contradictory output must fail closed."};r=c.get_use_request(1);c.assess_use_request(1,r["request_digest"]);assert c.get_use_request(1)["status"]=="CONSENSUS_UNRESOLVED" and not calls
def test_replay_and_digest_attack_blocked(runtime):
 _,c,g,_,_,_=runtime;request(c,g);assert c.assess_use_request(1,"sha256:"+"0"*64)=="REQUEST_DIGEST_MISMATCH";r=c.get_use_request(1);c.assess_use_request(1,r["request_digest"]);assert c.assess_use_request(1,r["request_digest"])=="REQUEST_NOT_ASSESSABLE"
