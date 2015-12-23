# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='asignacio',
            field=models.CharField(default=b'', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='cpv',
            field=models.CharField(default=b'', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='data',
            field=models.CharField(default=b'', max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='descripcio',
            field=models.CharField(default=b'', max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='desert',
            field=models.BooleanField(default=b''),
        ),
        migrations.AlterField(
            model_name='lot',
            name='importiva',
            field=models.DecimalField(default=b'', max_digits=9, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='importsenseiva',
            field=models.DecimalField(default=b'', max_digits=9, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numero',
            field=models.IntegerField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numofertes',
            field=models.IntegerField(default=b'', blank=True),
        ),
    ]
