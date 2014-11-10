# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20141108_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usermail', models.EmailField(default=b'', max_length=60)),
                ('date', models.DateField()),
                ('chef', models.ForeignKey(to='db.Chef')),
                ('menu', models.ForeignKey(to='db.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
