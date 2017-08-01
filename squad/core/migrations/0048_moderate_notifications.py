# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_populate_projectstatus_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='moderate_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectstatus',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]