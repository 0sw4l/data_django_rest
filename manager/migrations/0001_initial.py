# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datos', models.TextField()),
                ('creado', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Informacion Recibida',
            },
        ),
    ]
