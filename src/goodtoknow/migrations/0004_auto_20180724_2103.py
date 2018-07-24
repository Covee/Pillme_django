# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-24 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goodtoknow', '0003_auto_20180703_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikegPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodtoknow.gPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_gpost', through='goodtoknow.LikegPost', to=settings.AUTH_USER_MODEL),
        ),
    ]
