# Generated by Django 2.2 on 2019-12-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_belt_app', '0002_auto_20191213_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='wish_des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='wish_name',
            new_name='item',
        ),
    ]
