# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170729_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='none', max_length=250, unique=True),
        ),
    ]