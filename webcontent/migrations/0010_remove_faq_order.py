# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcontent', '0009_faq_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='order',
        ),
    ]
