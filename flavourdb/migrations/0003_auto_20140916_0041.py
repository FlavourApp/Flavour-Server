# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavourdb', '0002_remove_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surName',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
