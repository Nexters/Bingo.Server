# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodManager', '0003_auto_20150210_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodinfohistory',
            old_name='food_id',
            new_name='food',
        ),
    ]
