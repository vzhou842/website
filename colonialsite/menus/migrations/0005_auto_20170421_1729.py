# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_auto_20170421_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='reviewingUser',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
