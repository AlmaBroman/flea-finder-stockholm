# Generated by Django 3.2.23 on 2024-02-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_remove_comment_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='map_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]