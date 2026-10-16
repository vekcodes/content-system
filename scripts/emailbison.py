#!/usr/bin/env python3
"""Read-only GET helper for the EmailBison campaign system. Reads .env (EMAILBISON_API_KEY, EMAILBISON_URL).
Usage: python3 scripts/emailbison.py /api/campaigns [out.json]"""
import json, sys, urllib.request
from pathlib import Path

def load_env():
    env = {}
    for line in (Path(__file__).resolve().parent.parent / ".env").read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1); env[k.strip()] = v.strip()
    return env

def get(path):
    env = load_env()
    req = urllib.request.Request(env["EMAILBISON_URL"].rstrip("/") + path,
        headers={"Authorization": "Bearer " + env["EMAILBISON_API_KEY"], "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

if __name__ == "__main__":
    data = get(sys.argv[1])
    if len(sys.argv) > 2: Path(sys.argv[2]).write_text(json.dumps(data))
    else: print(json.dumps(data, indent=1)[:4000])
