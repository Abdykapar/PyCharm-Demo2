# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-14 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0035_auto_20170512_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chance', models.DecimalField(decimal_places=4, default=0, max_digits=8)),
                ('bolum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Bolumder')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.MyTable')),
            ],
        ),
        migrations.AddField(
            model_name='averagebol',
            name='chanse',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]