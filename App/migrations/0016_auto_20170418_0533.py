# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_rayonexp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rayonexp',
            old_name='ExpRayon',
            new_name='ExpName',
        ),
    ]
