import importlib.util
from pathlib import Path
from conftest import *
def load_executor(runtime):
 _,_,g,_,_,_=runtime;g.vm=type("VM",(),{"UserError":ValueError});spec=importlib.util.spec_from_file_location("executor_test",Path("contracts/licensed_use_executor.py"));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m.LicensedUseExecutor("0x"+"9"*40),g
def test_only_guard_can_authorize(runtime):
 e,g=load_executor(runtime);assert e.authorize_use(1,1,1,REQUESTER,"sha256:"+"a"*64,"sha256:"+"b"*64,2000000000,"sha256:"+"c"*64)=="ONLY_LICENSE_LATCH"
def test_bound_consumer_can_consume_once(runtime):
 e,g=load_executor(runtime);sender(g,"0x"+"9"*40);r="sha256:"+"c"*64;assert e.authorize_use(1,1,1,REQUESTER,"sha256:"+"a"*64,"sha256:"+"b"*64,2000000000,r)=="AUTHORIZED";sender(g,OUTSIDER);assert e.consume_authorization(1,r)=="ONLY_BOUND_CONSUMER";sender(g,REQUESTER);assert e.consume_authorization(1,r)=="CONSUMED";assert e.consume_authorization(1,r)=="AUTHORIZATION_ALREADY_CONSUMED"
def test_executor_replay_fails(runtime):
 e,g=load_executor(runtime);sender(g,"0x"+"9"*40);a=(1,1,1,REQUESTER,"sha256:"+"a"*64,"sha256:"+"b"*64,2000000000,"sha256:"+"c"*64);assert e.authorize_use(*a)=="AUTHORIZED";assert e.authorize_use(*a)=="AUTHORIZATION_REPLAY"
