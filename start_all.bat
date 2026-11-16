@echo off
title SafeTrip AI Launcher
echo ========================================================
echo Starting SafeTrip AI (Backend on 8000 + Frontend on 5173)
echo ========================================================
start "SafeTrip AI - Backend Server (Port 8000)" cmd /k "cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"
timeout /t 3 /nobreak >nul
start "SafeTrip AI - Frontend Vite (Port 5173)" cmd /k "cd frontend && npm run dev"
echo Both servers started!
echo Frontend URL: http://localhost:5173
echo Backend API Docs: http://127.0.0.1:8000/docs

