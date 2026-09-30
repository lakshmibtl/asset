#!/usr/bin/env python3
"""
One-time fix: Change asset.status from 'Temporary' -> 'In Use'
for all assets that have an active assignment.
Run: python3 fix_temp_status.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset1.settings')
django.setup()

from asset_app.models import Asset, Assignment

active_asset_ids = list(
    Assignment.objects.filter(
        status__in=['In Use', 'Temporary', 'Temporary Use']
    ).values_list('asset_id', flat=True)
)

count = Asset.objects.filter(
    id__in=active_asset_ids,
    status='Temporary'
).update(status='In Use')

print(f"✅ Fixed {count} asset(s): status 'Temporary' → 'In Use'")
