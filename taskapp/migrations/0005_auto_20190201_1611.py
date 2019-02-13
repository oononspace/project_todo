# Generated by Django 2.1.3 on 2019-02-01 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_auto_20190201_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='detail',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 16, 11, 21, 276875), verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 16, 11, 21, 276822), verbose_name='期日'),
        ),
    ]