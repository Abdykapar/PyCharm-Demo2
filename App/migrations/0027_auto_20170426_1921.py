# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-26 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_auto_20170424_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytable',
            name='NomTerciha',
            field=models.IntegerField(default=0),
        ),
    ]