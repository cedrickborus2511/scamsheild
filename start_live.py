import subprocess
import threading
import time
import re
import os
import sys
import uvicorn
from api.index import app
from fastapi.staticfiles import StaticFiles

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Mount root directory for static assets
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")

# 1. Start server thread
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
time.sleep(2)

print("[*] Local server running on http://127.0.0.1:8000")

# 2. Start cloudflared tunnel with retry logic
def start_tunnel():
    while True:
        print("[*] Starting cloudflared tunnel...")
        cmd = ["cloudflared.exe", "tunnel", "--url", "http://127.0.0.1:8000"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, encoding="utf-8")

        live_url = None
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            # Match only user subdomains, NEVER api.trycloudflare.com
            match = re.search(r"https://([a-zA-Z0-9-]+)\.trycloudflare\.com", line)
            if match:
                subdomain = match.group(1).lower()
                if subdomain != "api":
                    live_url = match.group(0)
                    with open("live_url.txt", "w", encoding="utf-8") as f:
                        f.write(live_url)
                    print("\n" + "="*60)
                    print(f">> LIVE PUBLIC DEMO URL: {live_url}")
                    print("="*60 + "\n")
        
        proc.wait()
        print("[!] Tunnel disconnected. Reconnecting in 3 seconds...")
        time.sleep(3)

start_tunnel()
