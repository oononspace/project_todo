# Generated by Django 2.1.3 on 2019-02-01 01:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 10, 57, 9, 812947), verbose_name='作成び'),
        ),
        migrations.AlterField(
            model_name='task',
            name='staff',
            field=models.CharField(max_length=30, verbose_name='担当者'),
        ),
    ]