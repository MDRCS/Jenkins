# Generated by Django 3.1.12 on 2021-12-21 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0009_auto_20211221_1930"),
    ]

    operations = [
        migrations.RemoveField(model_name="survey", name="section",),
    ]
