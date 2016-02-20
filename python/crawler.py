#!/usr/bin/env python
import sys
import shutil
import urllib
import flickr
 
NUMBER_OF_IMAGES = 150
# page = 1
# per_page=number
 
def traverse(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o
        
def get_related_tags():
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_ids.txt') as f:
        lines = f.readlines()
    
    line_number = 0
    for line_number in lines:
        print line_number
        try:
            file = open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/tags.txt",'a')
            file.close()
        except:
            print("Could not create file")
            sys.exit(0)
            
        with open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/tags.txt",'a') as t:
            t.write(str(flickr.tags_getPhotoTags(line_number))+"\n")
               
def get_related_geodata():
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_ids.txt') as f:
        lines = f.readlines()
    
    line_number = 0
    for line_number in lines:
        try:
            file = open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/geo_data.txt",'a')
            file.close()
        except:
            print("Could not create file")
            sys.exit(0)
            
        with open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/geo_data.txt",'a') as t:
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
            
def print_image_id(IDS):
    try:
        file = open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_ids.txt",'a')
        file.close()
    except:
        print("Could not create file")
        sys.exit(0)
        
    with open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_ids.txt",'a') as f:
        for ID in IDS:
            f.write(str(ID)+'\n')

def print_image_url(URLS):
    try:
        file = open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/URLS.txt",'a')
        file.close()
    except:
        print("Could not create file")
        sys.exit(0)
        
    with open("C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/URLS.txt",'a') as f:
        for URL in URLS:
            f.write(str(URL)+'\n')
                
def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print "You must specify at least one tag"
        return 1

    tags = []
    for item in args:
        tags.append(item)
    
    urls = get_urls_for_tags(tags, NUMBER_OF_IMAGES)
    ids = get_image_id(urls)
    print_image_url(urls)
    print_image_id(ids)    
    tag = get_related_tags()
    location = get_related_geodata()
 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))