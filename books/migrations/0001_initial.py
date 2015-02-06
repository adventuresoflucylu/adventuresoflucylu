# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllBooks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.PositiveSmallIntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('datepublished', models.DateField()),
                ('content', tinymce.models.HTMLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TheBigJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('number', models.PositiveSmallIntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('datepublished', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
