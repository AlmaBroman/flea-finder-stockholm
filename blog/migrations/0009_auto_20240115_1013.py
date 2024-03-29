# Generated by Django 3.2.23 on 2024-01-15 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20240115_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.TimeField(default='00:00:00'),
            preserve_default=False,
        ),
    ]
