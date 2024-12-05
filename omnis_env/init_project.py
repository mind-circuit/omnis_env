# init_project.py

import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(content)
        print(f"Created file: {path}")

def main():
    # Define project structure
    directories = [
        'omnis',
        'omnis/data',
        'omnis/models',
        'omnis/scripts',
        'omnis/contracts',
        'omnis/tests',
        'omnis/docs',
        'omnis/agents',
    ]

    files = {
        'omnis/README.md': "# Omnis\n",
        'omnis/.gitignore': "__pycache__/\n.env\n",
        'omnis/requirements.txt': "",
        'omnis/setup.py': "",
        'omnis/scripts/__init__.py': "",
        'omnis/agents/__init__.py': "",
        'omnis/tests/__init__.py': "",
    }

    # Create directories
    for directory in directories:
        create_directory(directory)

    # Create files
    for file_path, content in files.items():
        create_file(file_path, content)

    print("Project structure initialized.")

if __name__ == "__main__":
    main()
