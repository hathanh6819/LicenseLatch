#!/usr/bin/env node
import{createAccount,generatePrivateKey}from'../frontend/node_modules/genlayer-js/dist/index.js';
import{writeFileSync,existsSync,readFileSync}from'node:fs';
const target=new URL('./.test-wallet.env',import.meta.url);
const existing=existsSync(target)?readFileSync(target,'utf8').trim().split('=',2)[1]:'';
if(/^0x[0-9a-fA-F]{64}$/.test(existing)){
  const key=existing;
  console.log(`test_wallet.address=${createAccount(key).address}`);
  console.log('test_wallet.secret=existing local ignored file');
}else{
  const key=generatePrivateKey(),account=createAccount(key);
  writeFileSync(target,`TEST_WALLET_PRIVATE_KEY=${key}\n`,{encoding:'utf8',mode:0o600,flag:'w'});
  console.log(`test_wallet.address=${account.address}`);
  console.log('test_wallet.secret=created local ignored file');
}
