# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersubmit', '0015_auto_20170914_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersubmit.Post'),
        ),
    ]