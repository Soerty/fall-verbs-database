# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('words', '0005_auto_20170315_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Class'),
        ),
    ]
