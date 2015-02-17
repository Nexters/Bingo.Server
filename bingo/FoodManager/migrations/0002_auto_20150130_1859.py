# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrafoodlist',
            name='food_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='food_name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='icon_img_path1',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodinfo',
            name='icon_img_path2',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodmanager',
            name='manager_id',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foodmanager',
            name='password',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
