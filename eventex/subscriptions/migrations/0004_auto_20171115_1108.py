# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]
