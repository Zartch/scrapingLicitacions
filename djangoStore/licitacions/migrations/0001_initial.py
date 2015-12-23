# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.CharField(max_length=80)),
                ('organdeC', models.CharField(max_length=80, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contracte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('codiexpedient', models.CharField(max_length=80, blank=True)),
                ('tipusexpedient', models.CharField(max_length=30, blank=True)),
                ('tipuscontracte', models.CharField(max_length=15, blank=True)),
                ('subtipuscontracte', models.CharField(max_length=20, blank=True)),
                ('procediment', models.CharField(max_length=40, blank=True)),
                ('descripcio', models.TextField(blank=True)),
                ('presupostIVA', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('presupostSENSEIVA', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('percentIVA', models.DecimalField(max_digits=4, decimal_places=2, blank=True)),
                ('durada', models.CharField(max_length=30, blank=True)),
                ('ambitgeografic', models.CharField(max_length=30, blank=True)),
                ('termini', models.CharField(max_length=30, blank=True)),
                ('observacions', models.CharField(max_length=150, blank=True)),
                ('valorestimat', models.CharField(max_length=80, blank=True)),
                ('subhasta', models.BooleanField()),
                ('oberturapliques', models.CharField(max_length=80, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.CharField(max_length=15)),
                ('denominacio', models.CharField(max_length=90, blank=True)),
                ('nacionalitat', models.CharField(max_length=30, blank=True)),
                ('nif', models.CharField(max_length=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('numero', models.IntegerField(blank=True)),
                ('descripcio', models.CharField(max_length=150, blank=True)),
                ('data', models.DateField(blank=True)),
                ('cpv', models.CharField(max_length=80, blank=True)),
                ('importiva', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('importsenseiva', models.DecimalField(max_digits=9, decimal_places=2, blank=True)),
                ('desert', models.BooleanField()),
                ('numofertes', models.IntegerField(blank=True)),
                ('asignacio', models.CharField(max_length=80, blank=True)),
            ],
        ),
    ]
