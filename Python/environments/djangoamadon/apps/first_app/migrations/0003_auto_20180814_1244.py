# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-14 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20180814_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product',
        ),
    ]