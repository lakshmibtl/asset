from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0026_asset_added_by_alter_asset_series_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='processor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='graphic_card',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
