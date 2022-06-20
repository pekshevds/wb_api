from time import sleep
from .models import Brand, Collection, Color, Consist, Content, Country, Kind, Option, Season, Si, WBSize
from .models import Parent
from .models import Object

import requests
import json

from threading import Thread

#import asyncio

WB_HOST = 'https://suppliers-api.wildberries.ru'
WB_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6IjU0YzUzZjY3LTg5ODctNDk2Yy04ZjY4LTMxYWYyOTJiNTc2MiJ9.03JMjSl8VQXnbB18lSLt5hjhiHdpHQAcN11TfY9zq_I'

def get_elements_count(dir_name='/brands'):

    headers = {
            'Authorization': WB_TOKEN,
            'Content-Type': 'application/json; charset=utf-8',
    }
    result = requests.get(WB_HOST + '/api/v1/directory/get/list', headers=headers,)

    count = 0    
    if 200 <= result.status_code < 300:
        data = json.loads(result.content)
        count = data.get('data').get(dir_name)

    return count




def get_dir_from_wb(dir_name='/brands'):
     
    headers = {
        'Authorization': WB_TOKEN,
        'Content-Type': 'application/json; charset=utf-8',
    }

    params = {
        'top': get_elements_count(dir_name),
    }

    result = requests.get(WB_HOST + '/api/v1/directory' + dir_name, headers=headers, params=params)

    items = []
    if 200 <= result.status_code < 300:
        data = json.loads(result.content)
        items = data.get('data')

    return items

def update_dir(dir_name='/brands', Dir_Class=Brand):

    list_for_create = []
    list_for_update = []

    for dict in get_dir_from_wb(dir_name):
                
        name = dict.get('key')
        items = Dir_Class.objects.filter(name=name)
        
        if items.count() > 0:
            
            item = items[0]
            item.name = name
            list_for_update.append(item)
        else:
            
            item = Dir_Class()
            item.name = name
            list_for_create.append(item)

    Dir_Class.objects.bulk_create(list_for_create)
    Dir_Class.objects.bulk_update(list_for_update, fields=['name'])



def update_brands():
    
    update_dir()

def update_brands_in_thread():
    
    thread = Thread(target=update_brands)
    thread.start()
    
        

def get_parents_from_wb():
     
    headers = {
        'Authorization': WB_TOKEN,
        'Content-Type': 'application/json; charset=utf-8',
    }

    params = {
        'top': 1000000,
    }

    result = requests.get(WB_HOST + '/api/v1/config/get/object/parent/list', headers=headers, params=params)

    parents = []
    if 200 <= result.status_code < 300:
        data = json.loads(result.content)
        parents = data.get('data')

    return parents        
        
def update_parents():

    list_for_create = []
    list_for_update = []

    for name in get_parents_from_wb():
                
        #name = dict.get('key')
        items = Parent.objects.filter(name=name)
        
        if items.count() > 0:
            
            item = items[0]
            item.name = name
            list_for_update.append(item)
        else:
            
            item = Parent()
            item.name = name
            list_for_create.append(item)

    Parent.objects.bulk_create(list_for_create)
    Parent.objects.bulk_update(list_for_update, fields=['name'])



def get_objects_from_wb(parent=''):
     
    headers = {
        'Authorization': WB_TOKEN,
        'Content-Type': 'application/json; charset=utf-8',
    }

    params = {
        'parent': parent,
    }

    result = requests.get(WB_HOST + '/api/v1/config/object/byparent', headers=headers, params=params)

    objects = []
    if 200 <= result.status_code < 300:
        data = json.loads(result.content)
        objects = data.get('data')

    return objects

def update_objects(parent):
    
    for dict in get_objects_from_wb(parent=parent.name):
                
        name = dict.get('name')
        objects = Object.objects.filter(name=name, parent=parent)
        
        if objects.count() > 0:
            
            object = objects[0]
            object.name = name
            object.parent = parent
            object.save()
        else:
            
            object = Object()
            object.name = name
            object.parent = parent
            object.save()            



def update_collections():

    update_dir(dir_name='/collections', Dir_Class=Collection)

def update_collections_in_thread():

    thread = Thread(target=update_collections)
    thread.start()



def update_colors():

    update_dir(dir_name='/colors', Dir_Class=Color)

def update_colors_in_thread():

    thread = Thread(target=update_colors)
    thread.start()



def update_consists():

    update_dir(dir_name='/consists', Dir_Class=Consist)

def update_consists_in_thread():

    thread = Thread(target=update_consists)
    thread.start()



def update_contents():

    update_dir(dir_name='/contents', Dir_Class=Content)

def update_contents_in_thread():

    thread = Thread(target=update_contents)
    thread.start()



def update_countries():

    update_dir(dir_name='/countries', Dir_Class=Country)

def update_countries_in_thread():

    thread = Thread(target=update_countries)
    thread.start()



def update_kinds():

    update_dir(dir_name='/kinds', Dir_Class=Kind)

def update_kinds_in_thread():

    thread = Thread(target=update_kinds)
    thread.start()



def update_options():

    update_dir(dir_name='/options', Dir_Class=Option)

def update_options_in_thread():

    thread = Thread(target=update_options)
    thread.start()



def update_seasons():

    update_dir(dir_name='/seasons', Dir_Class=Season)

def update_seasons_in_thread():

    thread = Thread(target=update_seasons)
    thread.start()



def update_si():

    update_dir(dir_name='/si', Dir_Class=Si)

def update_si_in_thread():

    thread = Thread(target=update_si)
    thread.start()



def update_wbsizes():

    update_dir(dir_name='/wbsizes', Dir_Class=WBSize)

def update_wbsizes_in_thread():

    thread = Thread(target=update_wbsizes)
    thread.start()







def update_directories():
           
    update_parents()    
    for parent in Parent.objects.all():
        update_objects(parent=parent)