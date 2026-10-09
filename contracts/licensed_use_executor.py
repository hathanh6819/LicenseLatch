# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json,re
from datetime import datetime
ADDRESS=re.compile(r"^0x[0-9a-f]{40}$");SHA256=re.compile(r"^sha256:[0-9a-f]{64}$")
def canon(v):return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def sender():return str(gl.message.sender_address).lower()
def now():return int(datetime.fromisoformat(str(gl.message_raw["datetime"]).replace("Z","+00:00")).timestamp())
class LicensedUseExecutor(gl.Contract):
    guard:str;authorization_count:u256;indexes:TreeMap[str,str]
    def __init__(self,guard:str):
        g=guard.strip().lower()
        if not ADDRESS.fullmatch(g):raise gl.vm.UserError("INVALID_GUARD")
        self.guard=g;self.authorization_count=u256(0);self.indexes=TreeMap[str,str]()
    @gl.public.write
    def authorize_use(self,permission_id:u256,license_id:u256,request_id:u256,consumer:str,policy_digest:str,request_digest:str,expires_at:u256,receipt:str)->str:
        if sender()!=self.guard:return "ONLY_LICENSE_LATCH"
        c=consumer.strip().lower();r=receipt.strip().lower()
        if not ADDRESS.fullmatch(c) or not SHA256.fullmatch(policy_digest.lower()) or not SHA256.fullmatch(request_digest.lower()) or not SHA256.fullmatch(r):return "INVALID_AUTHORIZATION"
        key="auth:"+str(int(permission_id))
        if self.indexes.get(key,"")!="":return "AUTHORIZATION_REPLAY"
        if int(expires_at)<=now():return "AUTHORIZATION_EXPIRED"
        self.indexes[key]=canon({"permission_id":int(permission_id),"license_id":int(license_id),"request_id":int(request_id),"consumer":c,"policy_digest":policy_digest.lower(),"request_digest":request_digest.lower(),"receipt":r,"status":"ACTIVE","authorized_at":now(),"consumed_at":0,"expires_at":int(expires_at)});self.indexes["receipt:"+r]=str(int(permission_id));self.authorization_count=u256(int(self.authorization_count)+1);return "AUTHORIZED"
    @gl.public.write
    def consume_authorization(self,permission_id:u256,expected_receipt:str)->str:
        key="auth:"+str(int(permission_id));raw=self.indexes.get(key,"")
        if raw=="":return "AUTHORIZATION_NOT_FOUND"
        x=json.loads(raw)
        if sender()!=x["consumer"]:return "ONLY_BOUND_CONSUMER"
        if x["status"]!="ACTIVE":return "AUTHORIZATION_ALREADY_CONSUMED"
        if expected_receipt.strip().lower()!=x["receipt"]:return "RECEIPT_MISMATCH"
        if now()>=x["expires_at"]:return "AUTHORIZATION_EXPIRED"
        x["status"]="CONSUMED";x["consumed_at"]=now();self.indexes[key]=canon(x);return "CONSUMED"
    @gl.public.view
    def get_authorization(self,permission_id:u256)->dict:
        raw=self.indexes.get("auth:"+str(int(permission_id)),"");return json.loads(raw) if raw else {}
    @gl.public.view
    def get_protocol(self)->dict:return {"name":"LicensedUseExecutor","version":1,"guard":self.guard,"semantics":"guard-issued, consumer-bound, expiring, one-time authorization"}
Contract=LicensedUseExecutor
