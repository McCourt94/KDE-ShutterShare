'''
Created on Feb 18, 2016

@author: Stephen McCourt
'''
import json
import sys
import shutil
import urllib
import pprint
from ast import literal_eval
import os

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o
 
def read_image_ids():
    lines =  list()
    with open(os.getcwd()+'image_ids.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_tags():
    lines=list()
    with open(os.getcwd()+'tags.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_geo():
    lines=list()
    with open(os.getcwd()+'geo_data.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    
    return images
    
def read_image_url():
    lines=list()
    with open(os.getcwd()+'urls.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    
    return images

def generate(i,u,desc,geo_lat,geo_lon):
    images = []
    for j in range(0,len(i)):
        photos_dict={ 'id': '',
                    'url':'',
                    'description':{},
                    'location':{'lat':'','lon':''},}
        photos_dict['id']=i[j]
        photos_dict['url']=u[j]
        photos_dict['description']=desc[j]
        photos_dict['location']['lat'] = geo_lat[j]
        photos_dict['location']['lon']=geo_lon[j]       
        images.append(photos_dict) 
                    
    return images

def main():  
    
    image_ids = read_image_ids()
    image_tags = read_image_tags()
    image_geo_data = read_image_geo()
    geo_data_lat = []
    geo_data_lon = []
    for i in image_geo_data:
        if 'None' in i:
            geo_data_lat.append(i)
            geo_data_lon.append(i)
        else:
            i.encode('ascii')
            data = str.split(i,',')
            geo_data_lat.append(str(data[0]).replace('[','').replace('u',''))
            geo_data_lon.append(str(data[1]).replace(']','').replace('u','').replace(' ',''))
    image_url = read_image_url()
    JSON = generate(image_ids, image_url, image_tags, geo_data_lat, geo_data_lon)
           
    
    with open(os.getcwd()+"image_json.json", "w") as outfile:
        json.dump(JSON, outfile, indent=4)


if __name__ == '__main__':
    sys.exit(main())