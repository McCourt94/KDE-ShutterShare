import numpy
import sys,os.path
import glob, json
from numpy import array
from itertools import islice
from math import radians, cos, sin, asin, sqrt
import utilities
import time

'''NO LONGER USING THIS AS PART OF THE API, DUE TO BEING OUTSIDE SCOPE OF PROJECT
DECIDED TO IMPLEMENT GRID INDEXING VIA GEOINDEX/GEOHASH BASED ON GRID INDEX SPATIAL SEARCHING INSTEAD
QUESTIONS HAD BEEN RISEN DUE TO THE INEFFICIENCY OF COMPARING EACH SINGLE POINT WITH 
THE DESIRED INPUT'''



def haversinee(point1, point2, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    AVG_EARTH_RADIUS = 6371  # in km
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

def find_distance(myLocation,arraySearch,radius):
    found_matches = []
    for location in arraySearch:
        mySearch = (location[1],location[0])
        if (haversinee(myLocation,mySearch) <= radius):
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
         
          
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        path_to_files = root+'/python/data/image_json.json'  
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
           
        for coords in data:
            if coords['lat'] != 'None':
                myArray.append((coords['lon'],coords['lat'],coords['url']))
 
        matches = find_distance(myLocation, myArray, radius) 
        data = list(utilities.traverse(matches))
        #return json.dumps(data)
        print("--- %s seconds ---" % (time.time() - start_time))      
      
if __name__ == '__main__':
    start_time = time.time()
    sys.exit(main(sys.argv))