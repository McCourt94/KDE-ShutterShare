import numpy
import sys,os.path
import glob, json
from numpy import array
from itertools import islice
import math
from haversine import haversine

def to_absolute(num):
    return abs(num) 


def find_distance(myLocation,arraySearch,radius):
    found_matches = []
    for location in arraySearch:
        mySearch = (location[1],location[0])
        if (haversine(myLocation,mySearch) <= radius):
            found_matches.append(location[2])
    print len(found_matches)
    return found_matches

def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print ("You must input a location")
        return 1
    else:
        split = args[0].split(',')
        myLocation = (float(split[0]),float(split[1]))
        radius = float(split[2])
        myArray =[]
         
          
        JSON = "/python/data/image_json.json"
           
        path_to_files = os.getcwd()+JSON
           
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
           
        for coords in data:
            if coords['location']['lat'] != 'None':
                myArray.append((coords['location']['lon'],coords['location']['lat'],coords['url']))
                    
            
            
        print len(myArray)
        
        matches = find_distance(myLocation, myArray, radius)      
           
      
if __name__ == '__main__':
    sys.exit(main(*sys.argv)) 



    
    

