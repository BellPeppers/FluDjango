# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweets', '0003_auto_20160228_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='adjacent',
            field=models.ManyToManyField(blank=True, null=True, related_name='_region_adjacent_+', to='Tweets.Region'),
        ),
    ]