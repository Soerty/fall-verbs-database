# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_class_components'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes'},
        ),
        migrations.AddField(
            model_name='class',
            name='class_type',
            field=models.CharField(blank=True, choices=[('физическое', 'физическое'), ('метафорическое', 'метафорическое')], max_length=30, null=True),
        ),
    ]
