# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-30 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codeeditor', '0014_historicalappmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFieldModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('des', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('param', models.CharField(blank=True, max_length=255, null=True)),
                ('is_null', models.BooleanField(default=True, help_text='\u662f\u5426\u4e3a\u7a7a')),
                ('is_filter', models.BooleanField(default=False, help_text='\u5141\u8bb8\u7b5b\u9009')),
                ('is_search', models.BooleanField(default=False, help_text='\u5141\u8bb8\u641c\u7d22')),
                ('default_value', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u9ed8\u8ba4\u503c')),
                ('choices_value', models.TextField(blank=True, null=True, verbose_name='\u9009\u62e9\u5185\u5bb9')),
                ('widget', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u90e8\u4ef6')),
                ('filters', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b5b\u9009\u6761\u4ef6')),
                ('is_abstract', models.BooleanField(default=False, verbose_name='\u662f\u5426\u521b\u5efa')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', '\u5df2\u521b\u5efa'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='codeeditor.TableModel')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical field model',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFileModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('file', models.TextField(max_length=100, verbose_name='\u6587\u4ef6')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', '\u5df2\u521b\u5efa'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical file model',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSereverModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('host_name', models.CharField(blank=True, max_length=50, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('host_ip', models.GenericIPAddressField(verbose_name='\u4e3b\u673a\u5730\u5740')),
                ('host_port', models.IntegerField(default=22, verbose_name='\u4e3b\u673a\u7aef\u53e3')),
                ('host_user', models.CharField(help_text='\u4e0d\u63a8\u8350\u4f7f\u7528root', max_length=50, verbose_name='\u7528\u6237\u540d')),
                ('host_password', models.CharField(max_length=255, verbose_name='\u7528\u6237\u5bc6\u7801')),
                ('project_path', models.CharField(default='~/projects', help_text='\u9ed8\u8ba4\u7528\u6237\u4e3b\u76ee\u5f55projects', max_length=255, verbose_name='\u5de5\u7a0b\u8def\u5f84')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', '\u5df2\u521b\u5efa'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical serever model',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTableModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('des', models.CharField(blank=True, max_length=25, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', '\u5df2\u521b\u5efa'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('app', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='codeeditor.AppModel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical table model',
            },
        ),
        migrations.AddField(
            model_name='fieldmodel',
            name='is_abstract',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u521b\u5efa'),
        ),
    ]
