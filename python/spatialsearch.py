'''
Author: Stephen McCourt
Title: Shuttershare
Description: Implements geo spatial searching
'''
import sys,os.path
import glob, json
import utilities
import time
from geoindex import GeoGridIndex, GeoPoint
from itertools import chain
import geohash

def find_distance(grid,myLocation,arraySearch,radius):
    myUrlArray = []
    for value in arraySearch:
        grid.add_point(GeoPoint(value[0],value[1], ref=value[2]))

    for point,distance in grid.get_nearest_points(myLocation,radius,'km'):
        image_dict = {'id':'',
                      'lat':'',
                      'lon':'',}
        image_dict['id'] = point.ref
        image_dict['lat'] = point.latitude
        image_dict['lon'] = point.longitude
        myUrlArray.append(image_dict)
        
    return myUrlArray

        
'''below reads in the latitude and longitude passed in from the web server, reads the JSON structure, stores those with 
geo coords, passes data to find distance function above'''
def main(argv):    
    if len(argv) == 0:
        print ("You must input a location")
        return 1
    else:
        myArray =[]
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        grid = GeoGridIndex(precision=4)
        myLocation = GeoPoint(float(argv[1]),float(argv[2]))
        radius = int(argv[3])
        path_to_files = root+'/python/data/image_json.json'
        
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
           
        for coords in data:
            if coords['lat'] != 'None':
                myArray.append((coords['lat'],coords['lon'],coords['url']))

        matches = find_distance(grid, myLocation, myArray, radius)
        
        return json.dumps(matches)
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))
