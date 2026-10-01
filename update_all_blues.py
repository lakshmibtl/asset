import os
import re

directories = [
    '/home/btl/asset11/asset_app/templates',
    '/home/btl/asset11/asset_management/templates'
]

# Replacement map for blue variants
replacements = [
    (r'(?i)#4361ee', '#07518a'),
    (r'(?i)#0d5cff', '#07518a'),
    (r'(?i)#2563eb', '#07518a'),
    (r'(?i)#1d4ed8', '#053f6d'),
    (r'(?i)#3b82f6', '#0969b0'), # Lighter version of the main blue
    (r'(?i)rgba\(\s*13\s*,\s*92\s*,\s*255', 'rgba(7, 81, 138'),
    (r'(?i)rgba\(\s*37\s*,\s*99\s*,\s*235', 'rgba(7, 81, 138'),
    (r'(?i)rgba\(\s*59\s*,\s*130\s*,\s*246', 'rgba(9, 105, 176')
]

for directory in directories:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                new_content = content
                for pattern, repl in replacements:
                    new_content = re.sub(pattern, repl, new_content)
                
                if content != new_content:
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {path}")
