# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20180626_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=20000)),
                ('images', models.ImageField(blank=True, null=True, upload_to='upload_images/introduce/%Y/%m')),
            ],
        ),
    ]