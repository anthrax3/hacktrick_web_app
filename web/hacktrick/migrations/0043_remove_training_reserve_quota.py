# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-04 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0042_auto_20180303_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='reserve_quota',
        ),
    ]