# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-15 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeeditor', '0003_auto_20171215_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='des',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='appmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='widget',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u90e8\u4ef6'),
        ),
        migrations.AlterField(
            model_name='tablemodel',
            name='des',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='tablemodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]