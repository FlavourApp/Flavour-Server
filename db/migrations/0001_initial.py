# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('lastname', models.CharField(default=b'', max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('phone', models.CharField(max_length=12)),
                ('picture', models.ImageField(default=b'', upload_to=b'')),
                ('description', models.CharField(default=b'', max_length=200)),
                ('bio', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChefBioFoodImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('chef', models.ForeignKey(to='db.Chef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('name', models.CharField(default=b'', max_length=60, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('lastname', models.CharField(default=b'', max_length=60)),
                ('address', models.CharField(default=b'', max_length=60)),
                ('phone', models.CharField(default=b'', max_length=12)),
                ('FBID', models.CharField(default=b'', max_length=60, blank=True)),
                ('email', models.EmailField(default=b'', max_length=60)),
                ('comuna', models.ForeignKey(to='db.Comuna')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=b'2015-10-10')),
                ('chef', models.ForeignKey(to='db.Chef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('precio', models.IntegerField(default=0)),
                ('preparationTime', models.IntegerField(default=0)),
                ('picture', models.ImageField(default=b'', max_length=200, upload_to=b'')),
                ('tipo', models.CharField(default=b'', max_length=200)),
                ('chef', models.ForeignKey(to='db.Chef')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('menu', models.ForeignKey(to='db.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usermail', models.CharField(max_length=60)),
                ('cantidad', models.IntegerField(default=1)),
                ('date', models.DateField(default=b'2015-10-10')),
                ('status', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
                ('useraddress', models.CharField(max_length=60)),
                ('userphone', models.CharField(max_length=60)),
                ('chef', models.ForeignKey(to='db.Chef')),
                ('menu', models.ForeignKey(to='db.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('surName', models.CharField(default=b'', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chef',
            name='comunas',
            field=models.ManyToManyField(to='db.Comuna'),
            preserve_default=True,
        ),
    ]
