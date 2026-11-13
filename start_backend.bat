@echo off
title SafeTrip AI - Backend Server
echo ========================================================
echo Starting SafeTrip AI FastAPI Backend Server on Port 8000
echo ========================================================
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
pause
