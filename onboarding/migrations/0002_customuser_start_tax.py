# Generated by Django 5.0.4 on 2024-09-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("onboarding", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="start_tax",
            field=models.BooleanField(default=False),
        ),
    ]
