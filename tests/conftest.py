import importlib.util,sys,types
from pathlib import Path
import pytest
PUBLISHER="0x"+"1"*40;REQUESTER="0x"+"2"*40;AUTHORITY="0x"+"3"*40;OUTSIDER="0x"+"4"*40;EXECUTOR="0x"+"5"*40;ATTESTATION="sha256:"+"a"*64
POLICY="Commercial merchandise is allowed under 25000 units annual revenue. Gambling, tobacco, weapons, alcohol promotion, sublicensing, and AI training are prohibited. Direct convention apparel sales are permitted worldwide."
USE="Print the licensed character on 500 convention T-shirts sold directly by the requester, with projected annual revenue of 12000 units. No sublicense or AI training is involved."
class TreeMap(dict):
 @classmethod
 def __class_getitem__(cls,_):return cls
class U256(int):pass
class ContractBase:pass
class Write:
 def __call__(self,fn):return fn
class Public:write=Write();view=staticmethod(lambda fn:fn)
class Nondet:
 def __init__(self):self.answer={"decision":"COMPATIBLE","reasons":[],"explanation":"The direct apparel use fits the authority-confirmed policy."};self.prompts=[]
 def exec_prompt(self,prompt,**_):self.prompts.append(prompt);return self.answer
class Eq:
 def __init__(self):self.forced=None
 def prompt_comparative(self,fn,*_,**__):return self.forced if self.forced is not None else fn()
class Emitter:
 def __init__(self,calls):self.calls=calls
 def emit(self,**_):return self
 def authorize_use(self,*args):self.calls.append(args);return "AUTHORIZED"
@pytest.fixture
def runtime(monkeypatch):
 n=Nondet();eq=Eq();calls=[];g=types.ModuleType("genlayer");g.__all__=["gl","u256","TreeMap","typing","Address"]
 g.gl=g;g.Contract=ContractBase;g.public=Public();g.nondet=n;g.eq_principle=eq;g.message=types.SimpleNamespace(sender_address=PUBLISHER);g.message_raw={"datetime":"2026-10-06T00:00:00+00:00"};g.u256=U256;g.TreeMap=TreeMap;g.typing=types.SimpleNamespace(Any=object);g.Address=lambda x:x;g.get_contract_at=lambda _:Emitter(calls)
 monkeypatch.setitem(sys.modules,"genlayer",g);spec=importlib.util.spec_from_file_location("license_latch_test",Path("contracts/license_latch.py"));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 return m,m.LicenseLatch(),g,n,eq,calls
def sender(g,a):g.message.sender_address=a
def license(c):return c.create_license("Convention merchandise license","0x"+"a"*40,"Collection-wide",POLICY,25000,2000000000,False,False,AUTHORITY,ATTESTATION,"https://example.org/authority-record",EXECUTOR)
def activate(c,g):license(c);sender(g,AUTHORITY);assert c.confirm_license_authority(1,1,ATTESTATION)=="ACTIVE"
def request(c,g,**kw):
 activate(c,g);lic=c.get_license(1);sender(g,REQUESTER);d=dict(license_id=1,expected_policy_digest=lic["policy_digest"],intended_use=USE,industry="Apparel",territory="Worldwide",expected_revenue=12000,sublicensing_requested=False,ai_training_requested=False,evidence_note="Synthetic test request for direct convention sales.",consumer_address=REQUESTER,expected_license_epoch=2);d.update(kw);return c.submit_use_request(**d)
