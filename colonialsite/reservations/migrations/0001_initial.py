# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 01:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(choices=[('EK', 'Elk Room'), ('DV', 'Del Vento Room'), ('LB', 'Library'), ('DH', 'Dining Hall'), ('TP', 'Taproom'), ('MV', 'Movie Room')], max_length=2)),
                ('start_date', models.DateTimeField(verbose_name='start date/time')),
                ('end_date', models.DateTimeField(verbose_name='end date/time')),
                ('description', models.TextField()),
                ('approved', models.CharField(choices=[('S', 'Submitted'), ('A', 'Approved'), ('D', 'Denied')], max_length=1)),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
