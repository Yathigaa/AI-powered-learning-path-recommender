# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### 1. Text Not Visible / Poor Contrast
**Problem**: Text appears faded or hard to read
**Solution**: ✅ **FIXED** - Enhanced CSS styling with vibrant colors and better contrast
- All text now uses high-contrast colors (#ffffff, #00d4ff)
- Sidebar labels are bright white with bold fonts
- Tab text uses vibrant blue (#00d4ff) for inactive tabs

### 2. Tab Styling Issues
**Problem**: Home and Chat Mode tabs have poor font/size/color
**Solution**: ✅ **FIXED** - Completely redesigned tab styling
- Active tabs: Gradient background with white text, 18px font, bold weight
- Inactive tabs: Dark background with cyan text (#00d4ff), 16px font
- Added hover effects and smooth transitions

### 3. Export, Feedback, Analytics Not Working
**Problem**: Tabs show errors or don't function
**Solution**: ✅ **FIXED** - Added proper error handling and imports
- All modules now import correctly
- Added try-catch blocks for graceful error handling
- Fixed missing dependencies and function calls

### 4. NLTK Data Missing Error
**Problem**: "Resource punkt_tab not found" error
**Solution**: ✅ **FIXED** - Automatic NLTK data download
- Added automatic download of required NLTK resources
- Includes punkt, punkt_tab, stopwords, wordnet, averaged_perceptron_tagger
- Downloads happen automatically on first run

### 5. Application Won't Start
**Problem**: Various startup errors
**Solution**: Use the provided startup scripts
```bash
# Easy startup
python run_app.py

# Windows batch file
start_app.bat

# PowerShell script
.\start_app.ps1
```

### 6. Dependencies Missing
**Problem**: Import errors for packages
**Solution**: Install all requirements
```bash
pip install -r requirements.txt
```

### 7. Port Already in Use
**Problem**: Port 8501 is already in use
**Solution**: Use a different port
```bash
streamlit run src/app.py --server.port 8502
```

## 🚀 Quick Fixes

### Restart Application
1. Stop the current app (Ctrl+C)
2. Run: `python run_app.py`
3. Open: `http://localhost:8501`

### Clear Cache
```bash
# Clear Streamlit cache
streamlit cache clear

# Clear Python cache
python -c "import streamlit as st; st.caching.clear_cache()"
```

### Reset Session State
- Refresh the browser page
- Or use the "Clear Cache" button in Streamlit's settings

## 📞 Support

If you're still experiencing issues:
1. Check the console output for specific error messages
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Try running individual modules to isolate issues:
   ```bash
   python -c "import sys; sys.path.append('src'); import app"
   ```

## ✅ What's Working Now

- ✅ Text visibility with vibrant colors
- ✅ Professional tab styling with hover effects
- ✅ All tabs functional (Home, Chat, Analytics, Export, Feedback)
- ✅ Automatic NLTK data download
- ✅ Error handling and recovery
- ✅ Easy startup scripts for Windows
- ✅ Professional UI with modern design