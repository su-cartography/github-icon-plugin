# -*- coding: utf-8 -*-
"""
Configuration file for Map Icons QGIS Plugin

This file contains configuration settings for the plugin, including Zenodo URLs
for downloading icons and metadata files.
"""

# Zenodo DOI and URLs
ZENODO_DOI = "10.5281/zenodo.16882205"
ZENODO_BASE_URL = "https://zenodo.org/record/16882205/files"

# File URLs on Zenodo
ICONS_ZIP_URL = f"{ZENODO_BASE_URL}/icons.zip"
METADATA_EXCEL_URL = f"{ZENODO_BASE_URL}/boston-workshop-icons.xlsx"

# Local cache directories
CACHE_DIR = "cache"
ICONS_CACHE_DIR = "cache/icons"
METADATA_CACHE_DIR = "cache/metadata"

# Plugin settings
MAX_ICONS_PER_ROW = 5
ICON_SIZE = 64
BUTTON_SIZE = 72
LABEL_MAX_WIDTH = 80
LABEL_MIN_HEIGHT = 20

# Label styling
LABEL_STYLE = """
QLabel {
    font-size: 9px; 
    font-weight: bold;
    color: #2c3e50; 
    background-color: #ecf0f1; 
    border: 1px solid #bdc3c7; 
    border-radius: 3px;
    padding: 2px;
}
"""
