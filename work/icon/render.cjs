const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:180,height:180}});
const svg=fs.readFileSync(process.argv[2],'utf8');
await p.setContent(`<html><body style="margin:0"><img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" width=180 height=180></body></html>`);
await p.screenshot({path:process.argv[3],omitBackground:true});
await p.setViewportSize({width:400,height:80});
await p.setContent(`<body style="margin:0;background:#dee1e6;display:flex;gap:16px;align-items:center;padding:12px;font:13px system-ui">${[16,32,64].map(s=>`<img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" width=${s} height=${s}>`).join('')}<span style="background:#fff;padding:6px 10px;border-radius:8px;display:flex;gap:6px;align-items:center"><img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" width=16 height=16>Studijní kvízy · Procvičo…</span></body>`);
await p.screenshot({path:process.argv[4]});await b.close();})();
