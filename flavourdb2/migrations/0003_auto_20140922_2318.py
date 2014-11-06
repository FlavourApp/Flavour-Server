# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flavourdb2', '0002_chef_chefbiofoodimage_comuna_menu_menuimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna',
            name='chefs',
        ),
        migrations.AddField(
            model_name='chef',
            name='comunas',
            field=models.ManyToManyField(to='flavourdb2.Comuna'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
