# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 04:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersubmit', '0008_post_users_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='synopsis',
        ),
    ]