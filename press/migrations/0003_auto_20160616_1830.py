# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0002_auto_20160616_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(default='UNDEFINED', max_length=200),
        ),
    ]