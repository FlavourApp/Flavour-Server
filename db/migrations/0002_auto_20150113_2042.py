# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='custom',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='status',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='subject',
        ),
    ]
