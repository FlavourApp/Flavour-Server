# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavourdb2', '0005_auto_20140924_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='FBID',
            field=models.CharField(default=b'', max_length=60, blank=True),
        ),
    ]
