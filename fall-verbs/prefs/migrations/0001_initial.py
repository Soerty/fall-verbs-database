# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref', models.CharField(max_length=64)),
            ],
        ),
    ]
