# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0028_auto_20170310_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='parpicipant_accept',
            new_name='participant_accept',
        ),
    ]
