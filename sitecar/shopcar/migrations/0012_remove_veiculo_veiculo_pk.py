# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcar', '0011_auto_20160514_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='veiculo_pk',
        ),
    ]
