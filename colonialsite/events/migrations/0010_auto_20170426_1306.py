# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_merge_20170426_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('IMs', 'IMs'), ('Friday Party', 'Friday Party'), ('Semiformal', 'Semiformal'), ('Study Break', 'Study Break'), ('Sophomore Dinner', 'Sophomore Dinner'), ('Language Table', 'Language Table'), ("Members' Nights", "Members' Nights"), ('Weekly Events', 'Weekly Events'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
