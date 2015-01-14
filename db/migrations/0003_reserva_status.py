# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20150113_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='status',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
