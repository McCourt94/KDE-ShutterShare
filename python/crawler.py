#!/usr/bin/env python
import sys
import shutil
import urllib
 
import flickr
 
NUMBER_OF_IMAGES = 56
 
#this is slow
def get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, per_page=number)
    urls = []
    for photo in photos:
        try:
            urls.append(photo.getURL(size='Large', urlType='source'))
        except:
            continue
    return urls
 
def get_image_id(urls):
    ids = []
    for url in urls:
        print url
        photo_id = url.split('/')[-1]
        ids.append(photo_id)
    return ids

def get_image_data(ids):
    photos = []
    for id in ids:
        photos.append(flickr.tags_getPhotoTags(id))
    return photos

def print_data(image_data):
    for data in image_data:
        print data
        
def get_image_location(ids):
    photo_location = []
    for id in ids:
        photo_id = flickr.Photo(id)
        photo_location.append(photo_id.getLocation())
    return photo_location
        
    
 
def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print "You must specify at least one tag"
        return 1
 
    tags = [item for item in args]
 
    urls = get_urls_for_tags(tags, NUMBER_OF_IMAGES)
    ids = get_image_id(urls)
    geo = get_image_location(ids)
    image_data = get_image_data(ids)
    print_data(geo)

 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))