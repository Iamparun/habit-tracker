# Generated by Django 5.1.1 on 2024-11-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_habit_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="description",
            field=models.TextField(default="no description"),
            preserve_default=False,
        ),
    ]
