# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0009_word_vocab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='vocab',
            field=models.TextField(blank=True, null=True),
        ),
    ]
