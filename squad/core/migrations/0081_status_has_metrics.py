# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_auto_20180810_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='has_metrics',
            field=models.BooleanField(default=False),
        ),
    ]