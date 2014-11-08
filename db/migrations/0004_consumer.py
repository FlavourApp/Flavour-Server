# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavourdb2', '0003_auto_20140922_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('lastname', models.CharField(default=b'', max_length=60)),
                ('address', models.CharField(default=b'', max_length=60)),
                ('phone', models.CharField(default=b'', max_length=12)),
                ('FBID', models.CharField(default=b'', max_length=60)),
                ('email', models.EmailField(default=b'', max_length=60)),
                ('comuna', models.ForeignKey(to='flavourdb2.Comuna')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
