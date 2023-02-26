# Generated by Django 4.1.4 on 2023-02-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contactus",
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
                ("fullname", models.CharField(blank=True, max_length=100, null=True)),
                ("mobileno", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("purpose", models.CharField(blank=True, max_length=200, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]