# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_reserva_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='tipo',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reserva',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reserva',
            name='useraddress',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='username',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='userphone',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
