# Generated by Django 3.0.2 on 2020-01-10 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoip', '0002_auto_20200110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoip',
            name='datecached',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
