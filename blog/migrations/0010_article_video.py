# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170814_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.BooleanField(default=False),
        ),
    ]