# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManager', '0002_auto_20150130_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInfoHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('history_type', models.IntegerField(default=0)),
                ('food_id', models.ForeignKey(to='FoodManager.FoodInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='foodinfo',
            old_name='rec_exp_date',
            new_name='rec_exp',
        ),
    ]
