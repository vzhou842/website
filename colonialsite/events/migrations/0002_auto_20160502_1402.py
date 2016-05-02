# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Closed', 'Closed'), ('Open', 'Open'), ('Hidden', 'Hidden')], default='Hidden', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
    ]
