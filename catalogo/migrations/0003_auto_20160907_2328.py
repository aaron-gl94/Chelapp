# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20160907_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_drink', to='catalogo.TypeProduct'),
        ),
    ]