# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160418_1144'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='affil',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='affil',
            name='user',
        ),
        migrations.DeleteModel(
            name='Affil',
        ),
    ]
