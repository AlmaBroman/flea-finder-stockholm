# Generated by Django 3.2.23 on 2023-12-06 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='google_maps_link',
            new_name='map_link',
        ),
    ]
