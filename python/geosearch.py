import numpy
import sys
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
    return found_matches

def main():
    myArray =[]
    
    path_to_files ="C:/Users/Stephen McCourt/Desktop/Final Year University/Computer Project/Knowledge & Data Engineering Project/python/data/"
    glob.glob(path_to_files)
    
    with open(path_to_files+'image_json.json') as data_file:    
        data = json.load(data_file)
    
    for coords in data:
        if coords['location']['lat'] == 'None':
            print ""
        else:
            myArray.append((coords['location']['lon'],coords['location']['lat'],coords['url']))
    
    
    print len(myArray)
    myLocation = (54.585369,-5.93285)
    radius = 1
    matches = find_distance(myLocation, myArray, radius)      
    print len(matches)
    
if __name__ == '__main__':
    sys.exit(main()) 



    
    

