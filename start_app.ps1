# PowerShell script to start AI-Powered Learning Path Recommender
Write-Host "🚀 Starting AI-Powered Learning Path Recommender..." -ForegroundColor Green
Write-Host ""
Write-Host "📱 The app will open at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "🔄 Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

# Change to script directory
Set-Location $PSScriptRoot

# Check if Python is available
try {
    python --version | Out-Null
    Write-Host "✅ Python is available" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python first." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Start the application
try {
    python run_app.py
} catch {
    Write-Host "❌ Error starting application: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
