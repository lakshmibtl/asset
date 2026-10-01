import os
import re

directories = [
    '/home/btl/asset11/asset_app/templates',
    '/home/btl/asset11/asset_management/templates'
]

for directory in directories:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                new_content = re.sub(r'(?i)#4361ee', '#07518a', content)
                new_content = re.sub(r'(?i)#0d5cff', '#07518a', new_content)
                new_content = re.sub(r'(?i)rgba\(\s*13\s*,\s*92\s*,\s*255\s*,', 'rgba(7, 81, 138,', new_content)
                
                if content != new_content:
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {path}")
