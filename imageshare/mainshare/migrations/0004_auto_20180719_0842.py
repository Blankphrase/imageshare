# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-19 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainshare', '0003_category_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='latitude',
            new_name='place',
        ),
        migrations.RemoveField(
            model_name='category',
            name='preview',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainshare.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(default='Lorem ipsum dolor sit amet,\nagam probatus indoctum cu quo.\nEst eu quod rationibus,\nnam platonem sententiae no.\nEu mel vero oporteat elaboraret.'),
        ),
    ]
