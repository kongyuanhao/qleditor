# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 10:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0004_auto_20171215_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldmodel',
            options={'permissions': (('view_fieldmodel', 'View FieldModel'),)},
        ),
        migrations.AlterModelOptions(
            name='serevermodel',
            options={'permissions': (('view_serevermodel', 'View SereverModel'),)},
        ),
        migrations.AlterModelOptions(
            name='tablemodel',
            options={'permissions': (('view_tablemodel', 'View TableModel'),)},
        ),
    ]
