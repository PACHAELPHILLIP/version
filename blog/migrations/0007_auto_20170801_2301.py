# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170801_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None, max_length=250, unique=True),
        ),
    ]
