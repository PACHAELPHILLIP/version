# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 08:43
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields
import usersubmit.models


class Migration(migrations.Migration):

    dependencies = [
        ('usersubmit', '0006_auto_20170904_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=usersubmit.models.get_image_filename, verbose_name='Image'),
        ),
    ]
