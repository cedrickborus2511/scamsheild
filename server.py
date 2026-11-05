"""
SCAM SHIELD - Local Web Application Server
Starts the FastAPI application with static files and API endpoints on http://127.0.0.1:8000
"""
import sys
import uvicorn
from api.index import app

if __name__ == "__main__":
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 60)
    print("  SCAM SHIELD - Local Web Server Active")
    print("  Access in browser: http://127.0.0.1:8000")
    print("=" * 60)
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
