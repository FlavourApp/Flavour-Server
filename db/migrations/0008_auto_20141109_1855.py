# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='pictureUrl',
            field=models.ImageField(upload_to=b'media/img'),
        ),
    ]
