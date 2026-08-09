from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

def parse_time(t_str):
    if not isinstance(t_str, str):
        raise ValueError
    if t_str.endswith('Z'):
        t_str = t_str[:-1] + '+00:00'
    return datetime.fromisoformat(t_str)

@app.post("/corroborate")
async def corroborate(request: Request):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    if not isinstance(data, dict):
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    claim = data.get("claim")
    if not isinstance(claim, dict) or not isinstance(claim.get("value"), str):
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    asOf = data.get("asOf")
    try:
        asOf_dt = parse_time(asOf)
    except Exception:
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    stalenessDays = data.get("stalenessDays")
    if not isinstance(stalenessDays, (int, float)) or isinstance(stalenessDays, bool):
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    sources = data.get("sources")
    if not isinstance(sources, list):
        return JSONResponse({"verdict": "invalid", "confidence": "low", "corroboratingSources": []})
        
    # Valid sources
    valid_sources = []
    allowed_types = {"dns", "ct_log", "registry", "archive", "scan"}
    
    for s in sources:
        if not isinstance(s, dict): continue
        if not isinstance(s.get("id"), str): continue
        if not isinstance(s.get("origin"), str): continue
        if not isinstance(s.get("value"), str): continue
        if not isinstance(s.get("observedAt"), str): continue
        if s.get("type") not in allowed_types: continue
        
        try:
            obs_dt = parse_time(s["observedAt"])
        except Exception:
            continue
            
        s["_obs_dt"] = obs_dt
        valid_sources.append(s)
        
    # Fresh sources
    fresh_sources = []
    for s in valid_sources:
        delta_sec = (asOf_dt - s["_obs_dt"]).total_seconds()
        if delta_sec <= stalenessDays * 86400:
            fresh_sources.append(s)
            
    # Contradicted
    contradicting_ids = []
    for s in fresh_sources:
        if s.get("authoritative") is True and s["value"] != claim["value"]:
            contradicting_ids.append(s["id"])
            
    if contradicting_ids:
        return JSONResponse({
            "verdict": "contradicted",
            "confidence": "low",
            "corroboratingSources": sorted(contradicting_ids)
        })
        
    # Supported
    supporting_sources = [s for s in fresh_sources if s["value"] == claim["value"]]
    
    origins = {}
    for s in supporting_sources:
        orig = s["origin"]
        if orig not in origins:
            origins[orig] = []
        origins[orig].append(s)
        
    representatives = []
    for orig, srcs in origins.items():
        best_src = min(srcs, key=lambda x: x["id"])
        representatives.append(best_src)
        
    if len(representatives) >= 2:
        types = set(s["type"] for s in representatives)
        confidence = "high" if len(types) >= 2 else "medium"
        return JSONResponse({
            "verdict": "supported",
            "confidence": confidence,
            "corroboratingSources": sorted(s["id"] for s in representatives)
        })
        
    # Unverified
    return JSONResponse({
        "verdict": "unverified",
        "confidence": "low",
        "corroboratingSources": []
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
