# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-24 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects_awards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='projects',
            new_name='profile',
        ),
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='poster_id',
            field=models.IntegerField(default=0),
        ),
    ]