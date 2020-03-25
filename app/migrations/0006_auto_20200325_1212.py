# Generated by Django 3.0.4 on 2020-03-25 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200325_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='first_name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 3, 25, 12, 12, 40, 894437)),
        ),
    ]
