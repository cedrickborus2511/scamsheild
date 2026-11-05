@echo off
chcp 65001 > nul
title SCAM SHIELD - Web Application
echo ========================================================
echo  Starting SCAM SHIELD Server...
echo ========================================================
echo.
echo Starting FastAPI Web Application on http://127.0.0.1:8000
echo Open your web browser and visit: http://127.0.0.1:8000
echo Press Ctrl+C in this window to stop the server.
echo.
python server.py
pause
