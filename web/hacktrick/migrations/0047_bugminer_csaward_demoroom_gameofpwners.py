# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 13:46
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import hacktrick.utils


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0046_auto_20180306_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugMiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300, verbose_name='Baslik')),
                ('text_area', ckeditor.fields.RichTextField(verbose_name='Metin')),
                ('image', models.ImageField(help_text='160x160', upload_to='events/', validators=[hacktrick.utils.validate_speaker_image_dimensions], verbose_name='Resim')),
                ('order', models.PositiveIntegerField(verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Bug Miner',
                'verbose_name_plural': 'Bug Miners',
            },
        ),
        migrations.CreateModel(
            name='CsAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300, verbose_name='Baslik')),
                ('text_area', ckeditor.fields.RichTextField(verbose_name='Metin')),
                ('image', models.ImageField(help_text='160x160', upload_to='events/', validators=[hacktrick.utils.validate_speaker_image_dimensions], verbose_name='Resim')),
                ('order', models.PositiveIntegerField(verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Cs Award',
                'verbose_name_plural': 'Cs Awards',
            },
        ),
        migrations.CreateModel(
            name='DemoRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300, verbose_name='Baslik')),
                ('text_area', ckeditor.fields.RichTextField(verbose_name='Metin')),
                ('image', models.ImageField(help_text='160x160', upload_to='events/', validators=[hacktrick.utils.validate_speaker_image_dimensions], verbose_name='Resim')),
                ('order', models.PositiveIntegerField(verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Demo Room',
                'verbose_name_plural': 'Demo Rooms',
            },
        ),
        migrations.CreateModel(
            name='GameOfPwners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=300, verbose_name='Baslik')),
                ('text_area', ckeditor.fields.RichTextField(verbose_name='Metin')),
                ('image', models.ImageField(help_text='160x160', upload_to='events/', validators=[hacktrick.utils.validate_speaker_image_dimensions], verbose_name='Resim')),
                ('order', models.PositiveIntegerField(verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Game Of Pwner',
                'verbose_name_plural': 'Game Of Pwners',
            },
        ),
    ]