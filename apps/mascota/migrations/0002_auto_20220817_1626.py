# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2022-08-17 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(to='mascota.Vacuna'),
        ),
    ]