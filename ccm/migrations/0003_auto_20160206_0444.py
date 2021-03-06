# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccm', '0002_campaign_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizer',
            old_name='number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='participant',
            old_name='number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='physicalgoal',
            old_name='date',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='virturalgoal',
            old_name='date',
            new_name='datetime',
        ),
        migrations.AlterField(
            model_name='physicalgoal',
            name='participants',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='virturalgoal',
            name='participants',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
