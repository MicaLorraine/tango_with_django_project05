# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20170910_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
