# -*- coding: utf-8 -*-
import scrapy
from licitacions.models import *
from scrapy_djangoitem import DjangoItem

class Contractant(DjangoItem):
    django_model = Contractant
class Contracte(DjangoItem):
    django_model = Contracte
class Lot(DjangoItem):
    django_model = Lot
class Empresa(DjangoItem):
    django_model = Empresa

# Dades de contractant y tipologia de contracte
    # Organ de contractació
    # print(response.css('#denominacio-contracte dd').xpath('text()').extract()[0].strip())
    # codi, tipusexpedient... [1,2,3... n]
# class Contractant(scrapy.Item):
#     organdeC = scrapy.Field()
#
# class Contracte(scrapy.Item):
#     url = scrapy.Field()
#     codiexpedient = scrapy.Field()
#     tipusexpedient = scrapy.Field()
#     tipuscontracte = scrapy.Field()
#     subtipuscontracte = scrapy.Field()
#     procediment = scrapy.Field()
#
#     #Dades del Contracte
#     descripcio = scrapy.Field()
#     presupostIVA = scrapy.Field()
#     presupostSENSEIVA = scrapy.Field()
#     percentIVA = scrapy.Field()
#     durada = scrapy.Field()
#     ambitgeografic = scrapy.Field()
#     termini = scrapy.Field()
#     observacions = scrapy.Field()
#     valorestimat = scrapy.Field()
#     subhasta = scrapy.Field()
#     oberturapliques = scrapy.Field()
#
# class Lot(scrapy.Item):
#     url = scrapy.Field()
#     numero = scrapy.Field()
#     descripcio = scrapy.Field()
#     data = scrapy.Field()
#     cpv = scrapy.Field()
#     importiva = scrapy.Field()
#     importsenseiva = scrapy.Field()
#     desert = scrapy.Field()
#     numofertes = scrapy.Field()
#     asignacio = scrapy.Field()
#
# class Empresa(scrapy.Item):
#     denominacio = scrapy.Field()
#     nacionalitat = scrapy.Field()
#     id = scrapy.Field()



