# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0002_auto_20180603_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='pills',
            name='editor_said',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pills',
            name='feature',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
