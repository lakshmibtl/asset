import sys

dashboard_path = "/home/btl/asset1/asset_app/templates/asset_app/dashboard.html"
scratch_path = "/home/btl/asset1/asset_app/templates/asset_app/scratch_admin.html"

with open(dashboard_path, "r") as f:
    dashboard_lines = f.readlines()

with open(scratch_path, "r") as f:
    scratch_lines = f.readlines()

# Replace lines 1012 (index 1012) up to 1778
new_lines = dashboard_lines[:1012] + scratch_lines + ["\n"] + dashboard_lines[1778:]

with open(dashboard_path, "w") as f:
    f.writelines(new_lines)

print("Replaced lines successfully.")
