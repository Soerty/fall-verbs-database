# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classcomponentrelation',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='classcomponentrelation',
            name='component',
        ),
        migrations.DeleteModel(
            name='ClassComponentRelation',
        ),
    ]
