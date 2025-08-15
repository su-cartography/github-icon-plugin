#!/usr/bin/env python3
"""
Script to generate resources.qrc file from icons.txt
"""

def generate_resources_qrc():
    """Generate resources.qrc file from icons.txt"""
    
    # Read the icons.txt file
    with open('icons.txt', 'r') as f:
        icon_files = [line.strip() for line in f if line.strip()]
    
    print(f"Found {len(icon_files)} icons")
    
    # Generate the resources.qrc content
    qrc_content = '''<RCC>
  <qresource prefix="/plugins/map_icons">
    <file>icon.png</file>
'''
    
    # Add each icon file
    for icon_file in icon_files:
        qrc_content += f'    <file>icons/{icon_file}</file>\n'
    
    qrc_content += '''  </qresource>
</RCC>'''
    
    # Write the resources.qrc file
    with open('resources.qrc', 'w') as f:
        f.write(qrc_content)
    
    print(f"Generated resources.qrc with {len(icon_files)} icons")
    print("Now run: pyrcc5 -o resources_rc.py resources.qrc")

if __name__ == "__main__":
    generate_resources_qrc() 