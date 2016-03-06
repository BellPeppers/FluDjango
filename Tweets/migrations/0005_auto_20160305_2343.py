# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweets', '0004_region_adjacent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='finalScore',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='tweetScore',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='score',
            field=models.FloatField(null=True),
        ),
    ]
