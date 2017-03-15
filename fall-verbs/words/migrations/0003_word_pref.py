# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prefs', '0002_auto_20170315_1751'),
        ('words', '0002_auto_20170307_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='prefs.Pref'),
            preserve_default=False,
        ),
    ]
