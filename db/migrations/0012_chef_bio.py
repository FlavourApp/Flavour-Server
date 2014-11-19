# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_auto_20141110_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='bio',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
