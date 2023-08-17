import os

# Function of Folders creation
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder with the name {folder_name} has been created.")

# Function of Files creation
def create_file(file_name, content=""):
    with open(file_name, "w") as file:
        file.write(content)
        print(f"File with the name {file_name} has been created.")

# Content of the diferents files
root_folder = "webpage"
index_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<link rel='stylesheet' href='styles/style.css'>
<script src='scripts/main.js'></script>
</head>
<body>
</body>
</html>"""
style_content = "/* CSS Styles */"
js_content = "// JavaScript"

create_folder(root_folder)

# Creation of index.html ---
create_file(os.path.join(root_folder, "index.html"), index_content)

# Creation of the styles folder and the style.css file ---
styles_folder = os.path.join(root_folder, "styles")
create_folder(styles_folder)
create_file(os.path.join(styles_folder, "style.css"), style_content)

# Creation of the scripts folder and the main.js file ---
scripts_folder = os.path.join(root_folder, "scripts")
create_folder(scripts_folder)
create_file(os.path.join(scripts_folder, "main.js"), js_content)

print("Folder and file structure created successfully.")
