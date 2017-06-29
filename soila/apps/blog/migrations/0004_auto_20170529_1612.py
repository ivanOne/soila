# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-29 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='image/posts/%Y/%m/%d/', verbose_name='Заглавная картинка'),
        ),
    ]
