# Generated by Django 4.2.1 on 2023-05-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]