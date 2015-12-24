# -*- coding: utf-8 -*-
import json


#Treu espais i guarda com a json.
class LicitgenePipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        for field in item:
            if isinstance(item[field],basestring):
                aux = item[field]
                aux = aux.strip()
                item[field] = aux
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class ItemPersistencePipeline(object):
    def process_item(self, item, spider):
        try:
             item_model = item_to_model(item)
        except TypeError:
            return item

        model, created = get_or_create(item_model)
        try:
            update_model(model, item_model)
        except Exception,e:
            return e
        return item

#Funciones para updatear los registros en la db de django
#http://stackoverflow.com/questions/23663459/how-to-update-djangoitem-in-scrapy
def item_to_model(item):
    model_class = getattr(item, 'django_model')
    if not model_class:
        raise TypeError("Item is not a `DjangoItem` or is misconfigured")

    return item.instance


def get_or_create(model):
    model_class = type(model)
    created = False
    try:
        obj = model_class.objects.get(primary=model.primary)
    except model_class.DoesNotExist:
        created = True
        obj = model  # DjangoItem created a model for us.

    return (obj, created)

from django.forms.models import model_to_dict

def update_model(destination, source, commit=True):
    pk = destination.pk

    source_dict = model_to_dict(source)
    for (key, value) in source_dict.items():
        setattr(destination, key, value)

    setattr(destination, 'pk', pk)

    if commit:
        destination.save()

    return destination