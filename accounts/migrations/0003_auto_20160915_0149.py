# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-15 06:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160915_0140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Perfil',
        ),
    ]
