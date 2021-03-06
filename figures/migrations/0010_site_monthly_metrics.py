# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-04-08 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('figures', '0009_mau_metrics'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteMonthlyMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('month_for', models.DateField()),
                ('active_user_count', models.IntegerField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ['-month_for', 'site'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='sitemonthlymetrics',
            unique_together=set([('month_for', 'site')]),
        ),
    ]
