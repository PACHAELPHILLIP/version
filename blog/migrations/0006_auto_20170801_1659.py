# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170730_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumnail',
            new_name='thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='favorited_by_version',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='source_logo',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sourcelink',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
