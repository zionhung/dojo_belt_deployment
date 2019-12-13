# Generated by Django 2.2 on 2019-12-13 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_belt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='granted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='dojo_belt_app.User'),
            preserve_default=False,
        ),
    ]