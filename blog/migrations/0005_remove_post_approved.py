# Generated by Django 3.2.23 on 2023-12-06 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_additional_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
    ]