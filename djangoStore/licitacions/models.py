from django.db import models

class Contractant(models.Model):
    primary = models.CharField(max_length=80,primary_key=True)
    organdeC = models.CharField(blank=True, max_length=80)

class Contracte(models.Model):
    contractant = models.CharField(max_length=80, default='')
    primary = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    codiexpedient = models.CharField(blank=True, max_length=80)
    tipusexpedient = models.CharField(blank=True, max_length=30)
    tipuscontracte = models.CharField(blank=True, max_length=15)
    subtipuscontracte = models.CharField(blank=True, max_length=20)
    procediment = models.CharField(blank=True, max_length=40)

    #Dades del Contracte
    descripcio = models.TextField(blank=True)
    presupostIVA = models.DecimalField(blank=True, max_digits=9,  decimal_places=2)
    presupostSENSEIVA = models.DecimalField(blank=True,  max_digits=9,  decimal_places=2)
    percentIVA = models.DecimalField(blank=True,  max_digits=4,  decimal_places=2)
    durada = models.CharField(blank=True, max_length=30)
    ambitgeografic = models.CharField(blank=True, max_length=30)
    termini = models.CharField(blank=True, max_length=30)
    observacions = models.CharField(blank=True, max_length=150)
    valorestimat = models.CharField(blank=True, max_length=80)
    subhasta = models.BooleanField(blank=True, )
    oberturapliques = models.CharField(blank=True, max_length=80)

class Lot(models.Model):
    primary = models.CharField( max_length=200)
    url = models.CharField( max_length=200)
    numero = models.CharField(default='', blank=True, max_length=80)
    descripcio = models.CharField(default='', blank=True, max_length=150)
    data = models.CharField(default='', blank=True, max_length=15)
    cpv = models.CharField(default='', blank=True, max_length=80)
    importiva = models.DecimalField(default=00.00, blank=True, max_digits=9,  decimal_places=2)
    importsenseiva = models.DecimalField(default=00.00, blank=True, max_digits=9,  decimal_places=2)
    desert = models.BooleanField(default=False, blank=True)
    numofertes = models.CharField(default='', blank=True, max_length=80)
    asignacio = models.CharField(default='', blank=True, max_length=80)

class Empresa(models.Model):
    primary = models.CharField(max_length=15)
    denominacio = models.CharField(blank=True, max_length=90)
    nacionalitat = models.CharField(blank=True, max_length=30)
    nif = models.CharField(blank=True, max_length=15)
