# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('GradComment', '0002_auto_20160119_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.TimeField(default=datetime.datetime(2016, 1, 19, 12, 57, 37, 279736, tzinfo=utc), verbose_name=datetime.datetime(2016, 1, 19, 12, 57, 37, 279736, tzinfo=utc)),
        ),
    ]