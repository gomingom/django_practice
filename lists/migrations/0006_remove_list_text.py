# Generated by Django 5.0.4 on 2024-08-25 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0005_alter_item_list"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="list",
            name="text",
        ),
    ]
