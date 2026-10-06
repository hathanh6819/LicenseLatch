import importlib.util,json,sys,types
from pathlib import Path
import pytest

PUBLISHER="0x1111111111111111111111111111111111111111";REQUESTER="0x2222222222222222222222222222222222222222";OUTSIDER="0x3333333333333333333333333333333333333333"
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
 def __init__(self):self.answer={"decision":"COMPATIBLE","reasons":[],"explanation":"The declared direct apparel use fits the sealed policy."};self.prompts=[]
 def exec_prompt(self,prompt,**_):self.prompts.append(prompt);return self.answer
class Eq:
 def __init__(self):self.forced=None
 def prompt_comparative(self,fn,*_,**__):return self.forced if self.forced is not None else fn()
@pytest.fixture
def runtime(monkeypatch):
 n=Nondet();eq=Eq();g=types.ModuleType("genlayer");g.__all__=["gl","u256","TreeMap","typing"]
 g.gl=g;g.Contract=ContractBase;g.public=Public();g.nondet=n;g.eq_principle=eq;g.message=types.SimpleNamespace(sender_address=PUBLISHER);g.message_raw={"datetime":"2026-10-06T00:00:00+00:00"};g.u256=U256;g.TreeMap=TreeMap;g.typing=types.SimpleNamespace(Any=object)
 monkeypatch.setitem(sys.modules,"genlayer",g);spec=importlib.util.spec_from_file_location("license_latch_test",Path("contracts/license_latch.py"));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 return m,m.LicenseLatch(),g,n,eq
def sender(g,a):g.message.sender_address=a
def license(c):return c.create_license("Convention merchandise license","0x"+"a"*40,"Collection-wide",POLICY,25000,2000000000,False,False)
def request(c,g,**kw):
 license(c);lic=c.get_license(1);sender(g,REQUESTER)
 d=dict(license_id=1,expected_policy_digest=lic["policy_digest"],intended_use=USE,industry="Apparel",territory="Worldwide",expected_revenue=12000,sublicensing_requested=False,ai_training_requested=False,evidence_note="Synthetic test request for direct convention sales.",expected_license_epoch=1);d.update(kw);return c.submit_use_request(**d)
