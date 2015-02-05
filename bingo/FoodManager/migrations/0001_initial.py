# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraFoodList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_name', models.TextField()),
                ('frequency', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_info', models.TextField()),
                ('etc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_name', models.TextField()),
                ('rec_exp_date', models.IntegerField(default=1)),
                ('icon_img_path1', models.TextField()),
                ('icon_img_path2', models.TextField()),
                ('frequency', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager_id', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoMixFoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_info', models.TextField()),
                ('food_id1', models.ForeignKey(related_name='food1', to='FoodManager.FoodInfo')),
                ('food_id2', models.ForeignKey(related_name='food2', to='FoodManager.FoodInfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='foodextrainfo',
            name='food_id',
            field=models.ForeignKey(to='FoodManager.FoodInfo'),
            preserve_default=True,
        ),
    ]
