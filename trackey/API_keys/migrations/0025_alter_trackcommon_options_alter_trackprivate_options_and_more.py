# Generated by Django 5.0.2 on 2024-04-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("API_keys", "0024_alter_agency_token"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="trackcommon",
            options={"ordering": ["-depart"]},
        ),
        migrations.AlterModelOptions(
            name="trackprivate",
            options={"ordering": ["-depart"]},
        ),
        migrations.AlterField(
            model_name="commonkey",
            name="acces",
            field=models.TextField(max_length=50),
        ),
    ]
