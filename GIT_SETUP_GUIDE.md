# Git Setup Guide for Map Icons QGIS Plugin

This guide provides step-by-step instructions for setting up Git and uploading your cleaned QGIS plugin code to a Git repository.

## Prerequisites

- Git installed on your system
- GitHub/GitLab account (or other Git hosting service)
- Basic familiarity with command line operations

## Step 1: Clean Up the Repository

### Remove Unnecessary Files
The following files and directories should be removed as they contain private data or are auto-generated:

```bash
# Remove data files (now stored on Zenodo)
rm -rf icons/
rm *.xlsx
rm *.csv
rm boston-workshop-icons.xlsx
rm uuid_icon_mapping.csv
rm icon_mapping.xlsx
rm icon-metadata-documentation.xlsx

# Remove auto-generated files
rm resources_rc.py
rm *.qrc

# Remove cache and temporary files
rm -rf __pycache__/
rm -rf cache/
rm .DS_Store

# Remove old documentation files
rm UUID_ICON_MAPPING_SUMMARY.md
rm METADATA_SETUP_GUIDE.md
rm PLUGIN_SUMMARY.md
rm icons.txt
```

### Verify Clean Structure
Your repository should now contain only these essential files:

```
map_icons/
├── __init__.py
├── map_icons.py
├── map_icons_dialog.py
├── map_icons_dialog_base.ui
├── config.py
├── data_manager.py
├── requirements.txt
├── README.md
├── .gitignore
├── icon.png
├── metadata.txt
└── help/ (if needed)
```

## Step 2: Initialize Git Repository

### Create New Git Repository
```bash
# Navigate to your plugin directory
cd /path/to/map_icons

# Initialize Git repository
git init

# Add all files to staging
git add .

# Make initial commit
git commit -m "Initial commit: Map Icons QGIS Plugin with Zenodo integration"
```

## Step 3: Create Remote Repository

### Option A: GitHub
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name: `map-icons-qgis-plugin`
5. Description: `A comprehensive QGIS plugin for map icons with automatic Zenodo integration`
6. Make it **Public** (recommended for open source)
7. **Do NOT** initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

### Option B: GitLab
1. Go to [GitLab](https://gitlab.com) and sign in
2. Click "New Project"
3. Choose "Create blank project"
4. Project name: `map-icons-qgis-plugin`
5. Description: `A comprehensive QGIS plugin for map icons with automatic Zenodo integration`
6. Make it **Public**
7. Click "Create project"

## Step 4: Connect and Push to Remote

### Add Remote Origin
```bash
# Add remote repository (replace with your actual URL)
git remote add origin https://github.com/YOUR_USERNAME/map-icons-qgis-plugin.git

# Verify remote
git remote -v
```

### Push to Remote
```bash
# Push to main branch
git branch -M main
git push -u origin main
```

## Step 5: Verify Upload

### Check Repository
1. Visit your repository URL
2. Verify all files are present
3. Check that sensitive data is not included
4. Verify README.md displays correctly

### Test Clone
```bash
# Test cloning in a different directory
cd /tmp
git clone https://github.com/YOUR_USERNAME/map-icons-qgis-plugin.git
cd map-icons-qgis-plugin
ls -la
```

## Step 6: Set Up Repository Settings

### Repository Settings (GitHub)
1. Go to your repository → Settings
2. **General**:
   - Add topics: `qgis`, `plugin`, `mapping`, `icons`, `zenodo`
   - Add description
3. **Features**:
   - Enable Issues
   - Enable Wiki (optional)
   - Enable Discussions (optional)

### Repository Settings (GitLab)
1. Go to your project → Settings
2. **General**:
   - Add topics: `qgis`, `plugin`, `mapping`, `icons`, `zenodo`
   - Add description
3. **Features**:
   - Enable Issues
   - Enable Wiki (optional)

## Step 7: Create Release

### Tag and Release
```bash
# Create a tag for the release
git tag -a v1.0.0 -m "Release version 1.0.0: Initial release with Zenodo integration"

# Push tags
git push origin --tags
```

### Create GitHub Release
1. Go to your repository → Releases
2. Click "Create a new release"
3. Tag: `v1.0.0`
4. Title: `Map Icons QGIS Plugin v1.0.0`
5. Description: Use the content from your README.md
6. Upload any additional assets if needed
7. Click "Publish release"

## Step 8: Ongoing Development

### Development Workflow
```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes
# ... edit files ...

# Commit changes
git add .
git commit -m "Add new feature: description"

# Push feature branch
git push origin feature/new-feature

# Create pull request (GitHub) or merge request (GitLab)
```

### Updating Dependencies
```bash
# Update requirements.txt if needed
pip freeze > requirements.txt

# Commit dependency updates
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
```

## Security Considerations

### What's Safe to Include
✅ **Safe for public repositories:**
- Source code
- Configuration files (without secrets)
- Documentation
- Requirements/dependencies
- UI definitions
- Plugin metadata

❌ **Never include in public repositories:**
- API keys or secrets
- Personal information
- Database credentials
- Private data files
- Large binary files (use Zenodo instead)

### Data Privacy
- All icon files are now hosted on Zenodo (DOI: 10.5281/zenodo.16882205)
- No personal data is included in the code
- Configuration uses public Zenodo URLs
- Cache directories are excluded via .gitignore

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
# Check if you have write access to the repository
git remote -v
# Verify the URL is correct and you have access
```

**Large File Push Fails**
```bash
# If you accidentally included large files
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch LARGE_FILE' \
  --prune-empty --tag-name-filter cat -- --all
```

**Merge Conflicts**
```bash
# Pull latest changes
git pull origin main

# Resolve conflicts manually
# Then commit and push
git add .
git commit -m "Resolve merge conflicts"
git push origin main
```

## Best Practices

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep under 50 characters for the first line
- Add details in the body if needed

### Branch Naming
- `main` - Production-ready code
- `develop` - Development branch
- `feature/feature-name` - New features
- `bugfix/issue-description` - Bug fixes
- `hotfix/critical-fix` - Urgent fixes

### Regular Maintenance
- Keep dependencies updated
- Review and update documentation
- Monitor issues and pull requests
- Regular security updates

## Next Steps

1. **Documentation**: Ensure your README.md is comprehensive
2. **Issues**: Set up issue templates for bug reports and feature requests
3. **Contributing**: Create CONTRIBUTING.md if you want external contributions
4. **License**: Verify your license file is appropriate
5. **CI/CD**: Consider setting up automated testing (optional)

## Support

If you encounter issues:
1. Check Git documentation
2. Review GitHub/GitLab help pages
3. Search for similar issues on Stack Overflow
4. Ask in QGIS community forums

---

**Congratulations!** Your QGIS plugin is now properly version controlled and available on a public Git repository. Users can easily install, contribute to, and stay updated with your plugin.
