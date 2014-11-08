# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_remove_comuna_fakename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='id',
        ),
        migrations.AlterField(
            model_name='comuna',
            name='name',
            field=models.CharField(default=b'', max_length=60, serialize=False, primary_key=True),
        ),
    ]
