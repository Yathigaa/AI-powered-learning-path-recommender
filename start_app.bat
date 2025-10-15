@echo off
echo 🚀 Starting AI-Powered Learning Path Recommender...
echo.
echo 📱 The app will open at: http://localhost:8501
echo 🔄 Press Ctrl+C to stop the application
echo.

cd /d "%~dp0"
python run_app.py

pause
