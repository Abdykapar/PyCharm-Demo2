# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20170418_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='RayonExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('ExpRayon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp_rayon', to='App.LkpRayon')),
            ],
        ),
    ]
