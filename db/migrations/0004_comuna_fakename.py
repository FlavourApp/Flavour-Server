# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_remove_comuna_fakename'),
    ]

    operations = [
        migrations.AddField(
            model_name='comuna',
            name='fakename',
            field=models.CharField(default=b'', max_length=60),
            preserve_default=True,
        ),
    ]
