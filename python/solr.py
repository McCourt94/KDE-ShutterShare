'''
Created on Feb 22, 2016

@author: Stephen McCourt
'''
from __future__ import print_function
import pysolr
import json
from pprint import pprint
import sys

def solr(data):
    solr = pysolr.Solr('http://localhost:8983/solr/test')
    
    solr.add(data)

    results = solr.search('Belfast',**{
                'hl': 'true',
                'hl.fragsize': 100,
                'rows': 100,
            })

    print("Saw {0} result(s).".format(len(results)))

    for result in results:
        print("The id is '{0}'".format(result['url']))
    
    
def main():
    with open('C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project\python/image_json.json') as data_file:    
        data = json.load(data_file)
    
    
    solr(data)
    
if __name__ == '__main__':
    sys.exit(main())