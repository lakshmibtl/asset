
with open('/home/btl/asset11/asset_app/templates/asset_app/view_assets.html', 'r') as f:
    content = f.read()

lines = content.split('\n')
fixed_lines = []
i = 0
fixes = 0

while i < len(lines):
    line = lines[i]
    open_count = line.count('{%')
    close_count = line.count('%}')

    if open_count > close_count:
        merged = line
        j = i + 1
        while j < len(lines) and merged.count('{%') > merged.count('%}'):
            merged = merged + ' ' + lines[j].strip()
            j += 1
        fixes += 1
        fixed_lines.append(merged)
        i = j
    else:
        fixed_lines.append(line)
        i += 1

result = '\n'.join(fixed_lines)
with open('/home/btl/asset11/asset_app/templates/asset_app/view_assets.html', 'w') as f:
    f.write(result)

print(f"Fixed {fixes} split template tags")
print(f"Lines before: {len(lines)}, Lines after: {len(fixed_lines)}")
