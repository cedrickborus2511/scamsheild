@echo off
chcp 65001 > nul
title SCAM SHIELD - Public Live Demo Launcher
echo ========================================================
echo  Launching SCAM SHIELD Public Live Demo...
echo ========================================================
echo.
echo Starting local FastAPI server + Cloudflare Secure Tunnel...
echo.
python start_live.py
pause
