# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_name',
            new_name='name',
        ),
    ]
