# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_auto_20141109_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='pictureUrl',
        ),
        migrations.AddField(
            model_name='menu',
            name='picture',
            field=models.ImageField(default=b'', max_length=200, upload_to=b''),
            preserve_default=True,
        ),
    ]
