# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20170420_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='card_month',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], default=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_year',
            field=models.IntegerField(choices=[(1, '2017'), (2, '2018'), (3, '2019'), (4, '2020'), (5, '2021'), (6, '2022'), (7, '2023'), (8, '2024'), (9, '2025'), (10, '2026'), (11, '2027'), (12, '2028')], default=1),
        ),
    ]