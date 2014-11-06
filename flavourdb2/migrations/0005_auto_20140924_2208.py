# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavourdb2', '0004_consumer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='FBID',
            field=models.CharField(default=b'', max_length=60, null=True),
        ),
    ]
