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
import glob


def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o
 
def read_image_ids(path):
    lines =  list()
    with open(str(path)+'image_ids.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_tags(path):
    lines=list()
    with open(str(path)+'tags.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_geo(path):
    lines=list()
    with open(str(path)+'geo_data.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    
    return images
    
def read_image_url(path):
    lines=list()
    with open(str(path)+'urls.txt') as f:
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
    
    
    path_to_files ="C:/Users/Stephen McCourt/Desktop/Final Year University/Computer Project/Knowledge & Data Engineering Project/python/data/"
    glob.glob(path_to_files)
    
    image_ids = read_image_ids(path_to_files)
    image_tags = read_image_tags(path_to_files)
    image_geo_data = read_image_geo(path_to_files)
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
    image_url = read_image_url(path_to_files)
    JSON = generate(image_ids, image_url, image_tags, geo_data_lat, geo_data_lon)
           
    
    with open(path_to_files+"image_json.json", "w") as outfile:
        json.dump(JSON, outfile, indent=4)


if __name__ == '__main__':
    sys.exit(main())