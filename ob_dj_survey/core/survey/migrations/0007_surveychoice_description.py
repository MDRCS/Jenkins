# Generated by Django 3.1.12 on 2021-12-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0006_auto_20211214_2201"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveychoice",
            name="description",
            field=models.TextField(default="", null=True),
        ),
    ]