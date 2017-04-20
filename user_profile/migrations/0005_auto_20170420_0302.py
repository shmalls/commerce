# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20170419_2244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0004_auto_20170420_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=100)),
                ('card_number', models.IntegerField(null=True)),
                ('card_name', models.CharField(blank=True, max_length=100)),
                ('card_month', models.IntegerField(null=True)),
                ('card_year', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='itemorder',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Order'),
        ),
    ]