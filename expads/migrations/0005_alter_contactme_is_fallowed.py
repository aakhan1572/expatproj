# Generated by Django 4.1.4 on 2023-02-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expads", "0004_remove_contactme_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactme",
            name="is_fallowed",
            field=models.CharField(
                default="Yet Not Followed This Message", max_length=100
            ),
        ),
    ]