'use strict';
const http=require('http');
const path=require('path');
const core=require(path.join(__dirname,'..','docs','atlas-space-core.js'));

function send(res,status,data){const body=JSON.stringify(data);res.writeHead(status,{'Content-Type':'application/json','Content-Length':Buffer.byteLength(body),'Access-Control-Allow-Origin':'*','Access-Control-Allow-Headers':'Content-Type','Access-Control-Allow-Methods':'GET,POST,OPTIONS'});res.end(body);}
function readJson(req){return new Promise((resolve,reject)=>{let body='';req.on('data',c=>{body+=c;if(body.length>1e6){reject(new Error('request too large'));req.destroy();}});req.on('end',()=>{if(!body)return resolve({});try{resolve(JSON.parse(body));}catch(e){reject(e);}});req.on('error',reject);});}

function createServer(){return http.createServer(async(req,res)=>{
  if(req.method==='OPTIONS')return send(res,204,{});
  const url=new URL(req.url,'http://localhost');
  if(req.method==='GET'&&url.pathname==='/health')return send(res,200,{ok:true,runtime:'ATLAS SPACE',version:core.VERSION,public_demo:true});
  if(req.method==='GET'&&url.pathname==='/api/scenarios')return send(res,200,{scenarios:core.SCENARIOS});
  if(req.method==='POST'&&url.pathname==='/api/run'){
    try{const body=await readJson(req);if(!core.SCENARIOS[body.scenario])return send(res,400,{error:'unknown scenario'});const state=core.runScenario(body.scenario,{run_id:`api-${body.scenario}-${Date.now().toString(36)}`});return send(res,200,core.missionPackage(state));}catch(e){return send(res,400,{error:'invalid json'});}
  }
  if(req.method==='POST'&&url.pathname==='/api/protected'){
    try{const body=await readJson(req);if(!core.SCENARIOS[body.scenario])return send(res,400,{error:'unknown scenario'});if(!core.TOOL_REGISTRY[body.tool]||core.TOOL_REGISTRY[body.tool].authority!=='PROTECTED')return send(res,400,{error:'tool is not a registered protected action'});const base=core.runScenario(body.scenario,{run_id:`api-protected-${Date.now().toString(36)}`});const state=core.requestProtectedAction(base,body.tool,'Reference API Authority Test');return send(res,200,core.missionPackage(state));}catch(e){return send(res,400,{error:'invalid json'});}
  }
  return send(res,404,{error:'not found'});
});}

if(require.main===module){const port=Number(process.env.PORT||8788);createServer().listen(port,()=>console.log(`ATLAS SPACE reference API listening on http://localhost:${port}`));}
module.exports={createServer};
