# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20170318_1529'),
        ('words', '0007_auto_20170318_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sense',
            name='word',
        ),
        migrations.RemoveField(
            model_name='example',
            name='sense',
        ),
        migrations.AddField(
            model_name='example',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Class'),
        ),
        migrations.AddField(
            model_name='example',
            name='word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.Word'),
        ),
        migrations.DeleteModel(
            name='Sense',
        ),
    ]
