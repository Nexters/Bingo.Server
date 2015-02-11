# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManager', '0004_auto_20150210_0205'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExtraFoodList',
            new_name='ExtraFood',
        ),
    ]
