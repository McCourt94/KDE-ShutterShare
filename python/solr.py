from __future__ import print_function
import pysolr
import json
from pprint import pprint
import sys
import os
import utilities
from ast import literal_eval
import glob


def solr(search_item,data):
    solr = pysolr.Solr('http://localhost:8983/solr/test')
    solr.add(data)
        
    image_dictionary = []
    for item in search_item:
        results = solr.search(item,**{
                    'hl': 'true',
                    'hl.fragsize': 100,
                    'rows': 100,})


        for result in results:
            image_dictionary.append((result['url']))
    return image_dictionary
    
def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print ("You must specify at least one tag")
        return 1
    else:
        search_item = []
        for item in args:
            search_item.append(item)
            
        JSON = "/python/data/image_json.json"
    
        path_to_files = 'C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project/python/data/image_json.json'
        
        
    
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)

        test = solr(search_item,data)
        data = list(utilities.traverse(test))
        
        return json.dumps(data)
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))