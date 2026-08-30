'use strict';
const assert=require('assert');
const {createServer}=require('../tools/atlas-space-server.js');

async function request(base,path,options={}){const res=await fetch(base+path,options);const data=await res.json();return {status:res.status,data};}

(async()=>{
  const server=createServer();
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const addr=server.address();
  const base=`http://127.0.0.1:${addr.port}`;
  try{
    let r=await request(base,'/health');assert.strictEqual(r.status,200);assert.strictEqual(r.data.ok,true);assert.strictEqual(r.data.runtime,'ATLAS SPACE');
    r=await request(base,'/api/scenarios');assert.strictEqual(r.status,200);assert.ok(r.data.scenarios.orbital);assert.ok(r.data.scenarios.surface);assert.ok(r.data.scenarios.adversarial);
    r=await request(base,'/api/run',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({scenario:'orbital'})});assert.strictEqual(r.status,200);assert.strictEqual(r.data.final_status,'MISSION_STABLE');
    r=await request(base,'/api/protected',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({scenario:'orbital',tool:'space.human.eva.initiate'})});assert.strictEqual(r.status,200);assert.strictEqual(r.data.final_status,'MISSION_HOLD');assert.strictEqual(r.data.authority.protected_action_denied,true);
    console.log('ATLAS SPACE server smoke tests passed');
  }finally{await new Promise(resolve=>server.close(resolve));}
})().catch(err=>{console.error(err);process.exit(1);});
