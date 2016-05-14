# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcar', '0006_auto_20160329_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='id',
        ),
        migrations.AddField(
            model_name='veiculo',
            name='veiculo_id',
            field=models.CharField(default=1, max_length=32, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='preco',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
