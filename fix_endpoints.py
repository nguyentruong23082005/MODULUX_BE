import os
import glob
import re

FRONTEND_DIR = r"c:\Ngườithu3\modulux-homes_FE\src\views\admin"

# Dictionary of replacements: { "old_pattern": "new_string" }
replacements = {
    r"'/api/v1/site/settings'": r"'/api/v1/site-settings/'",
    r"`/api/v1/site/settings/": r"`/api/v1/site-settings/",
    
    r"'/api/v1/site/partners'": r"'/api/v1/partners/'",
    r"`/api/v1/site/partners/": r"`/api/v1/partners/",
    
    r"'/api/v1/site/features'": r"'/api/v1/core-features/'",
    r"`/api/v1/site/features/": r"`/api/v1/core-features/",
    
    r"'/api/v1/site/contacts'": r"'/api/v1/contacts/'",
    
    r"'/api/v1/blogs/'": r"'/api/v1/posts/'",
    r"`/api/v1/blogs/": r"`/api/v1/posts/",
    
    r"'/api/v1/site/banners/admin'": r"'/api/v1/banners/'",
    r"'/api/v1/site/banners'": r"'/api/v1/banners/'",
    r"`/api/v1/site/banners/": r"`/api/v1/banners/"
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for old, new in replacements.items():
        new_content = re.sub(old, new, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"No changes: {os.path.basename(filepath)}")

def main():
    vue_files = glob.glob(os.path.join(FRONTEND_DIR, "*.vue"))
    js_files = glob.glob(os.path.join(FRONTEND_DIR, "*.js"))
    for file in vue_files + js_files:
        process_file(file)

if __name__ == "__main__":
    main()
