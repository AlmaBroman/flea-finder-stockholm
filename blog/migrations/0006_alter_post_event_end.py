# Generated by Django 3.2.23 on 2023-12-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_end',
            field=models.TimeField(),
        ),
    ]