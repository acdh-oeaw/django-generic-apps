# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-02 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocabs', '0002_auto_20170202_1030'),
        ('lunch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='how_was_it',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vocabs.SkosConcept'),
        ),
    ]