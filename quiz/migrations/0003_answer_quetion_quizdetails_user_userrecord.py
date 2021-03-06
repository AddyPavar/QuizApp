# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20161022_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('idanswer', models.IntegerField(primary_key=True, serialize=False)),
                ('idquiz', models.IntegerField(blank=True, null=True)),
                ('ans', models.CharField(blank=True, max_length=45, null=True)),
                ('yans', models.CharField(blank=True, db_column='yAns', max_length=45, null=True)),
            ],
            options={
                'db_table': 'answer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Quetion',
            fields=[
                ('idquetion', models.AutoField(primary_key=True, serialize=False)),
                ('idquiz', models.IntegerField()),
                ('q_d', models.CharField(max_length=45)),
                ('a', models.CharField(blank=True, db_column='A', max_length=45, null=True)),
                ('b', models.CharField(blank=True, db_column='B', max_length=45, null=True)),
                ('c', models.CharField(blank=True, db_column='C', max_length=45, null=True)),
                ('d', models.CharField(blank=True, db_column='D', max_length=45, null=True)),
                ('ans', models.CharField(blank=True, db_column='Ans', max_length=45, null=True)),
                ('marks', models.CharField(blank=True, db_column='marks', max_length=45, null=True)),
            ],
            options={
                'db_table': 'quetion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Quizdetails',
            fields=[
                ('idquiz', models.AutoField(primary_key=True, serialize=False)),
                ('creator', models.CharField(max_length=45)),
                ('timelimit', models.IntegerField(blank=True, db_column='timeLimit', null=True)),
                ('subject', models.CharField(blank=True, max_length=45, null=True)),
                ('total', models.CharField(blank=True, max_length=45, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('time', models.CharField(blank=True, db_column='Time', max_length=45, null=True)),
            ],
            options={
                'db_table': 'quizDetails',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.AutoField(db_column='idUser', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=45, unique=True)),
                ('pass_field', models.CharField(db_column='pass', max_length=45)),
                ('type', models.CharField(db_column='Type', max_length=45)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Userrecord',
            fields=[
                ('iduserrecord', models.IntegerField(db_column='iduserRecord', primary_key=True, serialize=False)),
                ('idquiz', models.IntegerField(blank=True, null=True)),
                ('iduser', models.IntegerField(blank=True, db_column='idUser', null=True)),
                ('score', models.IntegerField(blank=True, db_column='Score', null=True)),
                ('userrecordcol', models.CharField(blank=True, db_column='userRecordcol', max_length=45, null=True)),
            ],
            options={
                'db_table': 'userRecord',
                'managed': True,
            },
        ),
    ]
