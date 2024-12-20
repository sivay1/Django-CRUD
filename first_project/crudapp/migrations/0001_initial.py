# Generated by Django 5.1.3 on 2024-11-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Details",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("age", models.IntegerField(max_length=30)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
