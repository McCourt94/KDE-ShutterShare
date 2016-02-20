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

def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o
 
def read_image_ids():
    lines =  list()
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_ids.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_tags():
    lines=list()
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/tags.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    return images

def read_image_geo():
    lines=list()
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/geo_data.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    
    return images
    
def read_image_url():
    lines=list()
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/urls.txt') as f:
        lines = f.readlines()
    
    images = [i.replace('\n',"") for i in lines]
    
    return images

def generate(id,url,tags,geo,**photo_dictionary):
    images = []
    for i in range(0,len(id)):
        photo_dictionary['ID']=id[i]
        photo_dictionary['URL']=url[i]
        photo_dictionary['TAGS']=tags[i]
        location = geo[i].split()
        if 'None' in location:
            photo_dictionary['LATITUDE']='None'
            photo_dictionary['LONGTITUDE']='None'
        else:
            photo_dictionary['LATITUDE']=location[0]
            photo_dictionary['LONGTITUDE']=location[1]              
        images.append(photo_dictionary.copy())  
                    
    return images

def main():
    
    photos_dictionary={ 'ID': '',
                        'URL':'',
                        'TAGS':[],
                        'LATITUDE':'',
                        'LONGTITUDE':''}
    
    
    image_ids = read_image_ids()
    image_tags = read_image_tags()
    image_geo_data = read_image_geo()
    image_url = read_image_url()
    JSON = generate(image_ids, image_url, image_tags, image_geo_data,**photos_dictionary)
    
    with open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_json.json", "w") as outfile:
        json.dump(JSON, outfile, indent=4)


if __name__ == '__main__':
    sys.exit(main())