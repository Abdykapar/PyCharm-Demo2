# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-16 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sifra', models.IntegerField(default=0)),
                ('NameN', models.CharField(max_length=200)),
                ('Surname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
            ],
        ),
    ]
