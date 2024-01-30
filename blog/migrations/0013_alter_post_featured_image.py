# Generated by Django 3.2.23 on 2024-01-23 14:12

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20240123_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=django_resized.forms.ResizedImageField(crop=None, default='placeholder', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[1000, None], upload_to='blog/'),
        ),
    ]