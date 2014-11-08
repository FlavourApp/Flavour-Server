# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_comuna_fakename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='fakename',
        ),
    ]
