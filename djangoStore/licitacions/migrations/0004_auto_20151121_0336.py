# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0003_auto_20151119_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracte',
            name='contractant',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='lot',
            name='asignacio',
            field=models.CharField(default='', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='cpv',
            field=models.CharField(default='', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='data',
            field=models.CharField(default='', max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='descripcio',
            field=models.CharField(default='', max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='importiva',
            field=models.DecimalField(default=0.0, decimal_places=2, blank=True, max_digits=9),
        ),
        migrations.AlterField(
            model_name='lot',
            name='importsenseiva',
            field=models.DecimalField(default=0.0, decimal_places=2, blank=True, max_digits=9),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numero',
            field=models.CharField(default='', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numofertes',
            field=models.CharField(default='', max_length=80, blank=True),
        ),
    ]
