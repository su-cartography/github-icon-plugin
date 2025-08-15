#!/bin/bash

# Cleanup script for Map Icons QGIS Plugin Repository
# This script removes unnecessary files before uploading to Git

echo "🧹 Cleaning up Map Icons QGIS Plugin repository..."

# Remove data files (now stored on Zenodo)
echo "📁 Removing data files..."
rm -rf icons/ 2>/dev/null
rm -f *.xlsx 2>/dev/null
rm -f *.csv 2>/dev/null
rm -f boston-workshop-icons.xlsx 2>/dev/null
rm -f uuid_icon_mapping.csv 2>/dev/null
rm -f icon_mapping.xlsx 2>/dev/null
rm -f icon-metadata-documentation.xlsx 2>/dev/null

# Remove auto-generated files
echo "🔧 Removing auto-generated files..."
rm -f resources_rc.py 2>/dev/null
rm -f *.qrc 2>/dev/null

# Remove cache and temporary files
echo "🗑️ Removing cache and temporary files..."
rm -rf __pycache__/ 2>/dev/null
rm -rf cache/ 2>/dev/null
rm -f .DS_Store 2>/dev/null
rm -f .DS_Store? 2>/dev/null
rm -f ._* 2>/dev/null

# Remove old documentation files
echo "📚 Removing old documentation files..."
rm -f UUID_ICON_MAPPING_SUMMARY.md 2>/dev/null
rm -f METADATA_SETUP_GUIDE.md 2>/dev/null
rm -f PLUGIN_SUMMARY.md 2>/dev/null
rm -f icons.txt 2>/dev/null

# Remove build and distribution files
echo "🏗️ Removing build files..."
rm -rf build/ 2>/dev/null
rm -rf dist/ 2>/dev/null
rm -rf *.egg-info/ 2>/dev/null

# Remove Python cache files
echo "🐍 Removing Python cache files..."
find . -name "*.pyc" -delete 2>/dev/null
find . -name "*.pyo" -delete 2>/dev/null
find . -name "*.pyd" -delete 2>/dev/null

echo ""
echo "✅ Cleanup completed!"
echo ""
echo "📋 Remaining files:"
ls -la

echo ""
echo "🔍 Verify that only these essential files remain:"
echo "   - __init__.py"
echo "   - map_icons.py"
echo "   - map_icons_dialog.py"
echo "   - map_icons_dialog_base.ui"
echo "   - config.py"
echo "   - data_manager.py"
echo "   - requirements.txt"
echo "   - README.md"
echo "   - .gitignore"
echo "   - icon.png"
echo "   - metadata.txt"
echo "   - help/ (if needed)"
echo ""
echo "🚀 You can now proceed with Git setup using the GIT_SETUP_GUIDE.md"
