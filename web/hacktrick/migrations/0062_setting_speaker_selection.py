# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-09 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0061_setting_transportation'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='speaker_selection',
            field=models.BooleanField(default=False, verbose_name='Konuşmacı alanları:'),
        ),
    ]
