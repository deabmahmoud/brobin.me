# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20160131_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='new_tab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submenuitem',
            name='new_tab',
            field=models.BooleanField(default=False),
        ),
    ]
