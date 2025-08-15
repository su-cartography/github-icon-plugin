# -*- coding: utf-8 -*-
"""
Data Manager for Map Icons QGIS Plugin

This module handles downloading and caching of icons and metadata from Zenodo.
"""

import os
import zipfile
from pathlib import Path
import logging

# Try to import requests, but provide fallback if not available
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    logging.warning("requests library not available. Zenodo downloads will not work.")

from .config import (
    ICONS_ZIP_URL, 
    METADATA_EXCEL_URL, 
    CACHE_DIR, 
    ICONS_CACHE_DIR, 
    METADATA_CACHE_DIR
)

logger = logging.getLogger(__name__)


class DataManager:
    """
    Manages downloading and caching of plugin data from Zenodo.
    """
    
    def __init__(self, plugin_dir):
        """
        Initialize the data manager.
        
        Args:
            plugin_dir: Path to the plugin directory
        """
        self.plugin_dir = Path(plugin_dir)
        self.cache_dir = self.plugin_dir / CACHE_DIR
        self.icons_cache_dir = self.plugin_dir / ICONS_CACHE_DIR
        self.metadata_cache_dir = self.plugin_dir / METADATA_CACHE_DIR
        
        # Create cache directories if they don't exist
        self._ensure_cache_directories()
    
    def _ensure_cache_directories(self):
        """Create cache directories if they don't exist."""
        self.cache_dir.mkdir(exist_ok=True)
        self.icons_cache_dir.mkdir(exist_ok=True)
        self.metadata_cache_dir.mkdir(exist_ok=True)
    
    def download_file(self, url, local_path, description="file"):
        """
        Download a file from URL to local path.
        
        Args:
            url: URL to download from
            local_path: Local path to save to
            description: Description for logging
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not REQUESTS_AVAILABLE:
            logger.error(f"Cannot download {description}: requests library not available")
            logger.error("Please install requests: pip install requests")
            return False
            
        try:
            logger.info(f"Downloading {description} from {url}")
            
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            logger.info(f"Successfully downloaded {description} to {local_path}")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download {description}: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error downloading {description}: {e}")
            return False
    
    def download_and_extract_icons(self):
        """
        Download and extract icons from Zenodo.
        
        Returns:
            bool: True if successful, False otherwise
        """
        icons_zip_path = self.icons_cache_dir / "icons.zip"
        
        # Download icons zip file
        if not self.download_file(ICONS_ZIP_URL, icons_zip_path, "icons zip"):
            return False
        
        # Extract icons
        try:
            with zipfile.ZipFile(icons_zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.icons_cache_dir)
            
            # Remove the zip file after extraction
            icons_zip_path.unlink()
            
            logger.info("Successfully extracted icons")
            return True
            
        except zipfile.BadZipFile as e:
            logger.error(f"Failed to extract icons: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error extracting icons: {e}")
            return False
    
    def download_metadata(self):
        """
        Download metadata Excel file from Zenodo.
        
        Returns:
            bool: True if successful, False otherwise
        """
        metadata_path = self.metadata_cache_dir / "boston-workshop-icons.xlsx"
        return self.download_file(METADATA_EXCEL_URL, metadata_path, "metadata Excel file")
    
    def get_icons_directory(self):
        """
        Get the path to the icons directory.
        
        Returns:
            Path: Path to icons directory
        """
        return self.icons_cache_dir
    
    def get_metadata_file(self):
        """
        Get the path to the metadata file.
        
        Returns:
            Path: Path to metadata file
        """
        return self.metadata_cache_dir / "boston-workshop-icons.xlsx"
    
    def icons_exist(self):
        """
        Check if icons exist in cache.
        
        Returns:
            bool: True if icons exist, False otherwise
        """
        return self.icons_cache_dir.exists() and any(
            self.icons_cache_dir.glob("*.png")
        )
    
    def metadata_exists(self):
        """
        Check if metadata exists in cache.
        
        Returns:
            bool: True if metadata exists, False otherwise
        """
        return self.get_metadata_file().exists()
    
    def ensure_data_available(self):
        """
        Ensure all required data is available, downloading if necessary.
        
        Returns:
            bool: True if all data is available, False otherwise
        """
        success = True
        
        # Check and download icons if needed
        if not self.icons_exist():
            logger.info("Icons not found in cache, downloading from Zenodo...")
            if not self.download_and_extract_icons():
                success = False
        
        # Check and download metadata if needed
        if not self.metadata_exists():
            logger.info("Metadata not found in cache, downloading from Zenodo...")
            if not self.download_metadata():
                success = False
        
        return success
    
    def clear_cache(self):
        """Clear all cached data."""
        try:
            import shutil
            if self.cache_dir.exists():
                shutil.rmtree(self.cache_dir)
                logger.info("Cache cleared successfully")
        except Exception as e:
            logger.error(f"Failed to clear cache: {e}")
    
    def get_cache_info(self):
        """
        Get information about cached data.
        
        Returns:
            dict: Cache information
        """
        info = {
            'cache_dir': str(self.cache_dir),
            'icons_count': 0,
            'metadata_exists': False,
            'total_size': 0
        }
        
        if self.icons_cache_dir.exists():
            icon_files = list(self.icons_cache_dir.glob("*.png"))
            info['icons_count'] = len(icon_files)
            info['total_size'] = sum(f.stat().st_size for f in icon_files)
        
        info['metadata_exists'] = self.metadata_exists()
        
        return info
    
    def check_dependencies(self):
        """
        Check if required dependencies are available.
        
        Returns:
            dict: Dependency status information
        """
        dependencies = {
            'requests': REQUESTS_AVAILABLE,
            'openpyxl': False,
            'zipfile': True  # Built-in module
        }
        
        # Check if openpyxl is available
        try:
            import openpyxl
            dependencies['openpyxl'] = True
        except ImportError:
            dependencies['openpyxl'] = False
        
        return dependencies
    
    def get_installation_instructions(self):
        """
        Get installation instructions for missing dependencies.
        
        Returns:
            str: Installation instructions
        """
        deps = self.check_dependencies()
        instructions = []
        
        if not deps['requests']:
            instructions.append("Install requests: pip install requests")
        
        if not deps['openpyxl']:
            instructions.append("Install openpyxl: pip install openpyxl")
        
        if instructions:
            return "\n".join(instructions)
        else:
            return "All dependencies are available!"
