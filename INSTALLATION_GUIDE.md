# Installation Guide - Map Icons QGIS Plugin

This guide provides step-by-step instructions for installing and setting up the Map Icons QGIS Plugin after cloning from Git.

## 🎯 Quick Start

### For End Users (Recommended)
1. **Install via QGIS Plugin Manager** (easiest method)
2. **Plugin automatically downloads required data** from Zenodo
3. **Start using immediately**

### For Developers/Contributors
1. **Clone from Git** and install manually
2. **Install Python dependencies**
3. **Copy to QGIS plugins directory**

## 📋 Prerequisites

- **QGIS 3.0 or higher**
- **Python 3.6 or higher**
- **Internet connection** (for initial data download)
- **Git** (for cloning repository)

## 🚀 Method 1: QGIS Plugin Manager (Recommended)

### Step 1: Open QGIS
- Launch QGIS application
- Wait for QGIS to fully load

### Step 2: Access Plugin Manager
- Go to **Plugins** → **Manage and Install Plugins**
- Or click the **Plugins** button in the toolbar

### Step 3: Install Plugin
- Click **All** tab
- Search for "Map Icons"
- Click **Install Plugin**
- Wait for installation to complete

### Step 4: First Run
- Go to **Plugins** → **Map Icons** → **Map Icons**
- Plugin will automatically download icons and metadata from Zenodo
- Progress dialog will show download status
- Once complete, you can start using the plugin

## 🔧 Method 2: Manual Installation from Git

### Step 1: Clone Repository
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/map-icons-qgis-plugin.git
cd map-icons-qgis-plugin
```

### Step 2: Install Python Dependencies
```bash
# Install required Python packages
pip install -r requirements.txt

# Or install individually:
pip install openpyxl>=3.0.0
pip install requests>=2.25.0
```

### Step 3: Copy to QGIS Plugins Directory

#### Windows
```bash
# Copy to QGIS plugins directory
xcopy /E /I map_icons "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\"
```

#### macOS
```bash
# Copy to QGIS plugins directory
cp -r map_icons ~/Library/Application\ Support/QGIS/QGIS3/profiles/default/python/plugins/
```

#### Linux
```bash
# Copy to QGIS plugins directory
cp -r map_icons ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

### Step 4: Restart QGIS
- Close QGIS completely
- Reopen QGIS
- Go to **Plugins** → **Manage and Install Plugins**
- Find "Map Icons" and **Enable** it

### Step 5: First Run
- Go to **Plugins** → **Map Icons** → **Map Icons**
- Plugin will download required data from Zenodo
- Wait for download to complete

## 📦 Dependencies Explained

### Required Python Packages

#### 1. `openpyxl` (≥3.0.0)
- **Purpose**: Read Excel files containing icon metadata
- **Why needed**: Metadata is stored in Excel format on Zenodo
- **Install**: `pip install openpyxl`

#### 2. `requests` (≥2.25.0)
- **Purpose**: Download icons and metadata from Zenodo
- **Why needed**: Plugin fetches data from cloud storage
- **Install**: `pip install requests`

### QGIS Built-in Dependencies
- **PyQt**: Provided by QGIS (no installation needed)
- **QGIS Core**: Built into QGIS application

## 🔍 Troubleshooting

### Common Installation Issues

#### 1. "ModuleNotFoundError: No module named 'openpyxl'"
**Solution:**
```bash
pip install openpyxl
# Or in QGIS Python environment:
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install openpyxl
```

#### 2. "ModuleNotFoundError: No module named 'requests'"
**Solution:**
```bash
pip install requests
# Or in QGIS Python environment:
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install requests
```

#### 3. Plugin Not Appearing in QGIS
**Solutions:**
- Check if plugin is in correct directory
- Restart QGIS completely
- Check QGIS error log (View → Panels → Log Messages)
- Verify Python version compatibility

#### 4. Download Failures from Zenodo
**Solutions:**
- Check internet connection
- Verify Zenodo service status
- Check firewall/network settings
- Try clearing plugin cache

### QGIS-Specific Issues

#### Windows
```bash
# Use QGIS Python environment
C:\Program Files\QGIS 3.x\bin\python3.exe -m pip install openpyxl requests
```

#### macOS
```bash
# Use QGIS Python environment
/Applications/QGIS.app/Contents/MacOS/bin/python3 -m pip install openpyxl requests
```

#### Linux
```bash
# Use QGIS Python environment
/usr/bin/python3 -m pip install openpyxl requests
```

## 📱 Data Download Process

### What Gets Downloaded
1. **Icons**: PNG files in ZIP format (~3.5 MB)
2. **Metadata**: Excel file with icon information (~9 KB)

### Download Locations
- **Cache Directory**: `[plugin_dir]/cache/`
- **Icons**: `[plugin_dir]/cache/icons/`
- **Metadata**: `[plugin_dir]/cache/metadata/`

### Offline Use
- After first download, plugin works offline
- Data is cached locally for future use
- Cache can be cleared if needed

## 🧪 Testing Installation

### Verify Plugin Works
1. **Launch Plugin**: Plugins → Map Icons → Map Icons
2. **Check Data**: Should see icons loading automatically
3. **Test Selection**: Click on icons to see metadata
4. **Apply to Layer**: Select a point layer and apply icon

### Expected Behavior
- ✅ Plugin launches without errors
- ✅ Icons download automatically
- ✅ Icon grid displays correctly
- ✅ Metadata panel shows information
- ✅ Icons can be applied to layers

## 🔄 Updating the Plugin

### Automatic Updates
- Plugin checks for new data on startup
- Updates are downloaded automatically
- No manual intervention required

### Manual Updates
```bash
# Pull latest code
git pull origin main

# Clear cache to force re-download
# (Plugin will do this automatically if needed)
```

## 📞 Getting Help

### Check Logs
- **QGIS Log**: View → Panels → Log Messages
- **Python Console**: Plugins → Python Console
- **Plugin Output**: Look for "Map Icons" messages

### Common Support Channels
- **GitHub Issues**: Report bugs and feature requests
- **QGIS Forums**: General QGIS support
- **Documentation**: Check README.md and help files

### Debug Information
When reporting issues, include:
- QGIS version
- Operating system
- Python version
- Error messages
- Log output

## 🎉 Success!

Once you see the icon grid with labels like "university", "park", "coffee", etc., your installation is complete!

The plugin will now:
- ✅ Display icons with descriptive labels
- ✅ Show comprehensive metadata
- ✅ Allow icon selection and application
- ✅ Work offline after initial setup
- ✅ Automatically update when new data is available

---

**Need Help?** Check the troubleshooting section above or create an issue on GitHub!
