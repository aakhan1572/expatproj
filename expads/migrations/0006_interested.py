# Generated by Django 4.1.4 on 2023-02-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expads", "0005_alter_contactme_is_fallowed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interested",
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
                ("fullname", models.CharField(max_length=150)),
                ("contactno", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=150)),
                ("Description", models.CharField(max_length=100)),
                (
                    "is_fallowed",
                    models.CharField(
                        default="Yet Not Followed This Message", max_length=100
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
