# Generated by Django 5.1.1 on 2024-11-18 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0003_alter_habit_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="description",
            field=models.TextField(default="No description"),
        ),
    ]
