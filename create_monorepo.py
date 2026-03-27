import os
import shutil
import subprocess

SRC_BE = r"c:\Ngườithu3\modulux-homes_BE"
SRC_FE = r"c:\Ngườithu3\modulux-homes_FE"
DEST_ROOT = r"c:\Ngườithu3\MODULUX_HOME"

def ignore_patterns(path, names):
    ignored = set()
    for name in names:
        if name in [".git", "venv", "node_modules", "__pycache__", ".vscode"]:
            ignored.add(name)
    return ignored

def main():
    if os.path.exists(DEST_ROOT):
        shutil.rmtree(DEST_ROOT, ignore_errors=True)
        
    os.makedirs(DEST_ROOT, exist_ok=True)
    
    print("Copying Backend...")
    shutil.copytree(SRC_BE, os.path.join(DEST_ROOT, "modulux-homes_BE"), ignore=ignore_patterns)
    
    print("Copying Frontend...")
    shutil.copytree(SRC_FE, os.path.join(DEST_ROOT, "modulux-homes_FE"), ignore=ignore_patterns)

    print("Initializing Git Monorepo...")
    # Change current working directory to DEST_ROOT explicitly for all subprocess calls
    commands = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "chore: setup monorepo for Modulux Homes"],
        ["git", "branch", "-M", "main"],
        ["git", "remote", "add", "origin", "https://github.com/nguyentruong23082005/MODULUX_HOME.git"],
        ["git", "push", "-u", "origin", "main", "--force"]
    ]
    
    for cmd in commands:
        subprocess.run(cmd, cwd=DEST_ROOT, check=True)
        
    print("Monorepo created and pushed successfully!")

if __name__ == "__main__":
    main()
