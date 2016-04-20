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
                    'lat':'',
                    'lon':''}
        photos_dict['id']=i[j]
        photos_dict['url']=u[j]
        photos_dict['description']=desc[j]
        photos_dict['lat'] = geo_lat[j]
        photos_dict['lon']=geo_lon[j]       
        images.append(photos_dict) 
                    
    return images

def main():  
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   
    path_to_files = root+'/python/data/image_json.json'   
    image_ids = read_image_ids(os.getcwd()+'/python/data/')
    image_tags = read_image_tags(os.getcwd()+'/python/data/')
    image_geo_data = read_image_geo(os.getcwd()+'/python/data/')
    geo_data_lat = []
    geo_data_lon = []
    for i in image_geo_data:
        if 'None' in i:
            geo_data_lat.append(i)
            geo_data_lon.append(i)
        else:
            i.encode('ascii')
            data = str.split(i,',')
            geo_data_lat.append(float(str(data[0]).replace('[','').replace('u','').replace("'","").replace(",","")))
            geo_data_lon.append(float(str(data[1]).replace(']','').replace('u','').replace(' ','').replace("'","")))
    image_url = read_image_url(os.getcwd()+'/python/data/')
    JSON = generate(image_ids, image_url, image_tags, geo_data_lat, geo_data_lon)
           
    
    with open(path_to_files, "w") as outfile:
        json.dump(JSON, outfile, indent=4)


if __name__ == '__main__':
    sys.exit(main())