# Generated by Django 5.0.2 on 2024-04-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0023_agency_date_token_agency_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agency",
            name="token",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
