# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=1000)),
                ('organizers', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('number', models.IntegerField(default=0)),
                ('occupation', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('number', models.IntegerField(default=0)),
                ('occupation', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=1000)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(default='', max_length=1000)),
                ('achieved', models.BooleanField(default=False)),
                ('compaign', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ccm.Campaign')),
                ('participants', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ccm.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='VirturalGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=1000)),
                ('date', models.DateTimeField()),
                ('platform', models.CharField(default='', max_length=1000)),
                ('achieved', models.BooleanField(default=False)),
                ('compaign', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ccm.Campaign')),
                ('participants', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ccm.Participant')),
            ],
        ),
    ]
