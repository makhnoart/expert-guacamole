# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-11 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20190111_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
