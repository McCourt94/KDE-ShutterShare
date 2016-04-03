import numpy
import sys,os.path
import glob, json
from numpy import array
from itertools import islice
import math
import utilities
from haversine import haversine

def find_distance(myLocation,arraySearch,radius):
    found_matches = []
    for location in arraySearch:
        mySearch = (location[1],location[0])
        if (haversine(myLocation,mySearch) <= radius):
            found_matches.append(location[2])
    return found_matches

def main(argv):
    args = argv    
    if len(args) == 0:
        print ("You must input a location")
        return 1
    else:
        myLocation = (float(args[1]),float(args[2]))
        if (len(args) == 4):
            radius = args[3]
        else:
            radius = 0
            
        myArray =[]
         
          
        JSON = "/python/data/image_json.json"
           
        path_to_files = 'C:\Users\Stephen McCourt\Desktop\Final Year University\Computer Project\Knowledge & Data Engineering Project/python/data/image_json.json' 
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
           
        for coords in data:
            if coords['location']['lat'] != 'None':
                myArray.append((coords['location']['lon'],coords['location']['lat'],coords['url']))
 
        matches = find_distance(myLocation, myArray, radius) 
        data = list(utilities.traverse(matches))
        return json.dumps(data)      
      
if __name__ == '__main__':
    sys.exit(main(sys.argv))
