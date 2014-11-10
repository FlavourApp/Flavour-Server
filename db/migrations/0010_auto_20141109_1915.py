# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_auto_20141109_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='picture',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
    ]
