# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20141109_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='pictureUrl',
        ),
        migrations.AddField(
            model_name='chef',
            name='picture',
            field=models.ImageField(default=b'', upload_to=b'img'),
            preserve_default=True,
        ),
    ]
