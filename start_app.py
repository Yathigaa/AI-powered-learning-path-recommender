#!/usr/bin/env python3
"""
Startup script for AI-Powered Learning Path Recommender
This script ensures proper environment setup and launches the Streamlit app
"""

import os
import sys
import subprocess
import platform

def check_requirements():
    """Check if required packages are installed."""
    required_packages = ['streamlit', 'pandas']
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing required packages: {', '.join(missing_packages)}")
        print("Please install them using: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed")
    return True

def setup_environment():
    """Setup the environment for the application."""
    print("🔧 Setting up environment...")
    
    # Set working directory to src folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, 'src')
    
    if os.path.exists(src_dir):
        os.chdir(src_dir)
        print(f"📁 Changed to directory: {src_dir}")
    else:
        print(f"❌ Source directory not found: {src_dir}")
        return False
    
    # Set environment variables for better text display
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    return True

def launch_app():
    """Launch the Streamlit application."""
    print("🚀 Launching AI-Powered Learning Path Recommender...")
    print("=" * 60)
    print("The application will open in your default web browser.")
    print("If it doesn't open automatically, go to: http://localhost:8501")
    print("=" * 60)
    
    try:
        # Launch Streamlit with specific configuration
        cmd = [
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.headless", "false",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false"
        ]
        
        subprocess.run(cmd, check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching Streamlit: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you're in the correct directory")
        print("2. Check if Streamlit is installed: pip install streamlit")
        print("3. Try running manually: streamlit run app.py")
        return False
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
        return True
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function to start the application."""
    print("🎓 AI-Powered Learning Path Recommender")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return False
    
    # Setup environment
    if not setup_environment():
        return False
    
    # Launch application
    return launch_app()

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
