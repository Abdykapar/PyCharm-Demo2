# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_iv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iv',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Bolumder'),
        ),
    ]
