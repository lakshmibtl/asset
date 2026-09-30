from django.db import migrations

CANONICAL = ('In Use', 'Returned', 'Temporary', 'Temporary Use')


def repair_custom_deployment_status(apps, schema_editor):
    """Move custom 'Other' deployment statuses off Assignment.status and onto Asset.status.

    The assign form used to write the free-text value the user typed into
    Assignment.status. Assignment.status is a lifecycle state that every active
    query filters on, so those rows were excluded and the asset vanished from the
    View Assets page.
    """
    Assignment = apps.get_model('asset_app', 'Assignment')
    Asset = apps.get_model('asset_app', 'Asset')

    for assignment in Assignment.objects.exclude(status__in=CANONICAL).iterator():
        custom_status = (assignment.status or '').strip()
        if not custom_status:
            assignment.status = 'In Use'
            assignment.save(update_fields=['status'])
            continue

        assignment.status = 'In Use'
        assignment.save(update_fields=['status'])

        asset = Asset.objects.filter(pk=assignment.asset_id).first()
        if asset is not None and (asset.status or '').strip() != custom_status:
            asset.status = custom_status
            asset.save(update_fields=['status'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0029_alter_assignment_status'),
    ]

    operations = [
        migrations.RunPython(repair_custom_deployment_status, noop),
    ]