#!/usr/bin/env python3
"""
Startup script for AI-Powered Learning Path Recommender
This script ensures all dependencies are available and starts the Streamlit app.
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        'streamlit', 'pandas', 'nltk', 'plotly', 'fpdf2', 
        'scikit-learn', 'numpy', 'matplotlib', 'seaborn'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing_packages)
        print("✅ All packages installed!")
    else:
        print("✅ All dependencies are available!")

def main():
    """Main function to start the application."""
    print("🚀 Starting AI-Powered Learning Path Recommender...")
    
    # Check dependencies
    check_dependencies()
    
    # Change to the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Start Streamlit app
    print("🌐 Starting Streamlit application...")
    print("📱 The app will open at: http://localhost:8501")
    print("🔄 Press Ctrl+C to stop the application")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "src/app.py", 
            "--server.port", "8501", "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped. Thank you for using AI-Powered Learning Path Recommender!")

if __name__ == "__main__":
    main()