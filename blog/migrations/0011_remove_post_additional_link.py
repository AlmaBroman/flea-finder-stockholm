# Generated by Django 3.2.23 on 2024-01-23 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20240122_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='additional_link',
        ),
    ]