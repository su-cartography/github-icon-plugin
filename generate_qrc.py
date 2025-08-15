import os

icons_folder = "icons"
qrc_path = "resources.qrc"

# Make sure the directory exists
if not os.path.exists(icons_folder):
    print(f"Error: {icons_folder} directory does not exist.")
    exit()

# Check if we have PNG files in the folder
files = os.listdir(icons_folder)
if not files:
    print(f"Error: No PNG files found in {icons_folder}.")
    exit()

# Start writing the .qrc file
qrc_lines = ['<RCC>\n  <qresource prefix="/plugins/map_icons">\n']
for file in sorted(files):
    if file.endswith(".png"):
        qrc_lines.append(f'    <file>{icons_folder}/{file}</file>\n')

qrc_lines.append('  </qresource>\n</RCC>\n')

with open(qrc_path, "w") as f:
    f.writelines(qrc_lines)

print(f"Updated {qrc_path} with all icons.")
