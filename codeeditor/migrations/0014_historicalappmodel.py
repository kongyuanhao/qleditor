# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codeeditor', '0013_auto_20180112_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAppModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('des', models.CharField(blank=True, max_length=25, null=True)),
                ('img_path', models.CharField(blank=True, max_length=255, null=True)),
                ('server_port', models.IntegerField(blank=True, verbose_name='\u542f\u52a8\u7aef\u53e3')),
                ('created', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', '\u5df2\u521b\u5efa'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('server', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='codeeditor.SereverModel')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical app model',
            },
        ),
    ]
