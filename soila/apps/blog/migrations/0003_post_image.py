# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-29 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170527_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Заглавная картинка'),
        ),
    ]
