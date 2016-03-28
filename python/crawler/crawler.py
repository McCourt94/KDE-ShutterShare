#!/usr/bin/env python
import sys
import shutil
import urllib
import flickr
import os
import glob
 
NUMBER_OF_IMAGES = 150
 
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o
        
def get_related_tags(path):
    with open(path+'image_ids.txt') as f:
        lines = f.readlines()
    
    line_number = 0
    for line_number in lines:
        print line_number
        try:
            file = open(path+"tags.txt",'a')
            file.close()
        except:
            print("Could not create file")
            sys.exit(0)
            
        with open(path+"tags.txt",'a') as t:
            t.write(str(flickr.tags_getPhotoTags(line_number))+"\n")
               
def get_related_geodata(path):
    with open(path+"image_ids.txt") as f:
        lines = f.readlines()
    
    line_number = 0
    for line_number in lines:
        try:
            file = open(path+"geo_data.txt",'a')
            file.close()
        except:
            print("Could not create file")
            sys.exit(0)
            
        with open(path+"geo_data.txt",'a') as t:
            t.write(str(flickr.location_getPhotoLocation(line_number))+"\n")
                        
def get_urls_for_tags(tags, number):
    page_number = 1
    photos = []
    for page_number in range(1,11):       
        photos.append(flickr.photos_search(tags=tags, per_page=number, page=page_number))
    data = list(traverse(photos))
    urls = []
    for photo in data:
        try:
            urls.append(photo.getURL(size='Large', urlType='source'))
        except:
            continue
    return urls

def get_image_id(urls):
    ids = []
    for url in urls:
        #print url
        photo_id = url.split('/')[-1]
        ids.append(photo_id)
    return ids
            
def print_image_id(path,IDS):
    try:
        file = open(path+"image_ids.txt",'a')
        file.close()
    except:
        print("Could not create file")
        sys.exit(0)
        
    with open(os.getcwd()+"image_ids.txt",'a') as f:
        for ID in IDS:
            f.write(str(ID)+'\n')

def print_image_url(URLS,path):
    try:
        file = open(path+"URLS.txt",'a')
        file.close()
    except:
        print("Could not create file")
        sys.exit(0)
        
    with open(path+"URLS.txt",'a') as f:
        for URL in URLS:
            f.write(str(URL)+'\n')
                
def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print "You must specify at least one tag"
        return 1
    
    
    path_to_files = os.getcwd()+'/python/data/'
    tags = []
    for item in args:
        tags.append(item)
    
    urls = get_urls_for_tags(tags, NUMBER_OF_IMAGES)
    ids = get_image_id(urls)
    print_image_url(path_to_files,urls)
    print_image_id(path_to_files,ids)    
    tag = get_related_tags(path_to_files)
    location = get_related_geodata(path_to_files)
 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))