# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metamoudel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u5b57', max_length=255)),
                ('des', models.TextField(help_text='\u7b80\u4ecb')),
                ('module', models.ForeignKey(help_text='\u6a21\u5757_id', on_delete=django.db.models.deletion.CASCADE, related_name='functions', to='metamoudel.ModuleModel')),
            ],
        ),
        migrations.RemoveField(
            model_name='tablemodel',
            name='module',
        ),
        migrations.AddField(
            model_name='functionmodel',
            name='tables',
            field=models.ManyToManyField(related_name='functions', to='metamoudel.TableModel'),
        ),
    ]
