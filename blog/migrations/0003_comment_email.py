# Generated by Django 3.2.23 on 2023-12-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_google_maps_link_post_map_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='no_email', max_length=254),
            preserve_default=False,
        ),
    ]