# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='about',
        ),
    ]
