# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0008_auto_20170319_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='vocab',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
