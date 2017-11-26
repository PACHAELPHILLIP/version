# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170809_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Review', 'Review'), ('Version', 'Version'), ('Music', 'Music'), ('Fashion', 'Fashion'), ('Culture', 'Culture')], max_length=20),
        ),
    ]
