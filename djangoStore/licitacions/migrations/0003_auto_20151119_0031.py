# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licitacions', '0002_auto_20151119_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='desert',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numero',
            field=models.CharField(default=b'', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='lot',
            name='numofertes',
            field=models.CharField(default=b'', max_length=80, blank=True),
        ),
    ]
