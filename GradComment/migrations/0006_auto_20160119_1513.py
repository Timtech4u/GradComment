# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 14:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GradComment', '0005_auto_20160119_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='student_comment',
        ),
        migrations.AddField(
            model_name='students',
            name='student_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GradComment.Comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.TimeField(default=datetime.datetime(2016, 1, 19, 14, 13, 47, 352286, tzinfo=utc), verbose_name=datetime.datetime(2016, 1, 19, 14, 13, 47, 352286, tzinfo=utc)),
        ),
    ]
