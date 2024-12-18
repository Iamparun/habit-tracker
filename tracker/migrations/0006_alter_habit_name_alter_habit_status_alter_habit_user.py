# Generated by Django 5.1.1 on 2024-11-19 04:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0005_alter_habit_description_alter_habit_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="habit",
            name="status",
            field=models.CharField(
                choices=[("Pending", "Pending"), ("Completed", "Completed")],
                default="Pending",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
