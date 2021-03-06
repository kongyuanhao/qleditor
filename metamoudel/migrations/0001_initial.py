# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 14:28
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
            name='FieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u5b57', max_length=255)),
                ('des', models.TextField(help_text='\u7b80\u4ecb')),
                ('placeholder', models.TextField(help_text='\u63cf\u8ff0')),
                ('genre', models.CharField(help_text='\u540e\u7aef\u7c7b\u578b', max_length=255)),
                ('widget', models.CharField(help_text='\u524d\u6bb5\u90e8\u4ef6', max_length=255)),
                ('default_value', models.CharField(help_text='\u9ed8\u8ba4\u503c', max_length=255)),
                ('foreign_model', models.CharField(help_text='\u5916\u952e\u53c2\u6570', max_length=255)),
                ('is_null', models.BooleanField(help_text='\u662f\u5426\u4e3a\u7a7a')),
                ('is_search', models.BooleanField(help_text='\u662f\u5426\u641c\u7d22')),
                ('is_abstract', models.BooleanField(help_text='\u662f\u5426\u521b\u5efa')),
                ('filter_terms', models.CharField(help_text='\u67e5\u8be2\u6761\u4ef6', max_length=255)),
                ('error_msg', models.CharField(help_text='\u6821\u9a8c\u9519\u8bef\u63d0\u793a', max_length=255)),
                ('verify', models.CharField(help_text='\u5b57\u6bb5\u6821\u9a8c', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u5b57', max_length=255)),
                ('des', models.TextField(help_text='\u7b80\u4ecb')),
                ('create_time', models.DateTimeField(auto_now=True, help_text='\u521b\u5efa\u65f6\u95f4')),
                ('creator', models.ForeignKey(help_text='\u521b\u5efa\u8005', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u5b57', max_length=255)),
                ('des', models.TextField(help_text='\u7b80\u4ecb')),
                ('module', models.ForeignKey(help_text='\u6a21\u5757_id', on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='metamoudel.ModuleModel')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='\u540d\u5b57', max_length=255)),
                ('category', models.CharField(help_text='\u7c7b\u522b', max_length=255)),
                ('des', models.TextField(help_text='\u7b80\u4ecb')),
                ('create_time', models.DateTimeField(auto_now=True, help_text='\u521b\u5efa\u65f6\u95f4')),
                ('creator', models.ForeignKey(help_text='\u521b\u5efa\u8005', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='modulemodel',
            name='template',
            field=models.ForeignKey(help_text='\u6a21\u677f_id', on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='metamoudel.TemplateModel'),
        ),
        migrations.AddField(
            model_name='fieldmodel',
            name='table',
            field=models.ForeignKey(help_text='table_id', on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='metamoudel.TableModel'),
        ),
    ]
