# Generated by Django 4.2.6 on 2023-12-26 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InOut', '0006_asset_name_of_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='name_of_person',
        ),
    ]
