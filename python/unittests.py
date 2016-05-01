import unittest
from flask import Flask, Response, json, render_template, jsonify, make_response, request, current_app
import requests
import traceback
import random
import validictory
import math
from testfixtures import compare
from geoindex import GeoGridIndex, GeoPoint
from geoindex.utils import km_to_mi, mi_to_km
import geohash, pysolr, spatialsearch, generate_json, solr, server, flickr, crawler
import os

TEST_POINTS = (
    (50.44268, 30.51774),
    (50.432602, 30.520205),
    (50.428211, 30.49502),
    (50.457149, 30.54046),
    )

class TestSystem(unittest.TestCase):
    
    
    def test_spatial_search(self):
        grid = GeoGridIndex(precision=4)
        myLocation = GeoPoint(54.598671,-5.918605)
        myArray = [[54.600225,5.920579,"15664490410_3dc1a99796_b.jpg"],[54.598671,-5.918605,'14749709315_4b30a18a5f_b.jpg']]
        test = [{'lat':54.598671,'id':'14749709315_4b30a18a5f_b.jpg','lon':-5.918605}]
        radius = 4
        self.assertEqual(spatialsearch.find_distance(grid,myLocation,myArray,radius), test)
    
    def test_plot_grid(self):
        grid = GeoGridIndex(precision=4)
        for i in range(0,10):
            lat = random.random()*180 - 90
            lng = random.random()*360 - 180
            grid.add_point(GeoPoint(lat, lng))
        
        self.assertEqual(len(grid.data), 10)
        
    
    def test_convert_km_to_mi(self):
        self.assertEqual(km_to_mi(1), .621371192)
        self.assertEqual(km_to_mi(1.), .621371192)
        self.assertAlmostEqual(km_to_mi(1.609344), 1.)
        self.assertRaises(TypeError, km_to_mi, '1')

    def test_convert_mi_to_km(self):
        self.assertEqual(mi_to_km(1), 1.609344)
        self.assertEqual(mi_to_km(1.), 1.609344)
        self.assertAlmostEqual(mi_to_km(.621371192), 1.)
        self.assertRaises(TypeError, mi_to_km, '1')
    
    def test_geo_point(self):
        point = GeoPoint(*TEST_POINTS[0])
        self.assertEqual(point.latitude, TEST_POINTS[0][0])
        self.assertEqual(point.longitude, TEST_POINTS[0][1])
        self.assertIsNone(point._rad_latitude)
        self.assertIsNone(point._rad_longitude)

        self.assertEqual(point.rad_latitude, math.radians(TEST_POINTS[0][0]))
        self.assertEqual(point.rad_longitude, math.radians(TEST_POINTS[0][1]))
        self.assertIsNotNone(point._rad_latitude)
        self.assertIsNotNone(point._rad_longitude)
        self.assertEqual(point.rad_latitude, point._rad_latitude)
        self.assertEqual(point.rad_longitude, point._rad_longitude)

        same = GeoPoint(TEST_POINTS[0][0], TEST_POINTS[0][1])
        self.assertEqual(point, same)
        self.assertTrue(point == same)

        other = GeoPoint(TEST_POINTS[1][0], TEST_POINTS[1][1])
        self.assertNotEqual(point, other)
        self.assertFalse(point == other)

        self.assertNotEqual(point, TEST_POINTS[0])
        self.assertFalse(point == TEST_POINTS[0])
    
    def test_geo_point_distance(self):
        location_x = GeoPoint(*TEST_POINTS[0])
        location_y = GeoPoint(*TEST_POINTS[1])

        self.assertAlmostEqual(
            location_x.distance_to(location_y, 'mi'), .7046874859635269
        )
        self.assertAlmostEqual(
            location_x.distance_to(location_y, 'km'), 1.1340845774104864
        )  
        self.assertAlmostEqual(
            location_y.distance_to(location_x, 'mi'), .7046874859635269
        )
        self.assertAlmostEqual(
            location_y.distance_to(location_x, 'km'), 1.1340845774104864
        )
    
    def test_solr_return_100(self):
        solr = pysolr.Solr('http://localhost:8983/solr/keyword')
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_files = root+'/python/data/image_json.json'
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
        
        solr.add(data)
        
        results = solr.search("Belfast", **{
                'hl': 'true',
                'hl.fragsize': 100,
                'rows': 100,})
        
        self.assertEqual(len(results),100)
        
    def test_solr_return_200(self):
        solr = pysolr.Solr('http://localhost:8983/solr/keyword')
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_files = root+'/python/data/image_json.json'
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
        
        solr.add(data)
        
        results = solr.search("Belfast", **{
                'hl': 'true',
                'hl.fragsize': 200,
                'rows': 200,})
        
        self.assertEqual(len(results),200) 
        
    def test_solr_return_300(self):
        solr = pysolr.Solr('http://localhost:8983/solr/keyword')
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_files = root+'/python/data/image_json.json'
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
        
        solr.add(data)
        
        results = solr.search("Belfast", **{
                'hl': 'true',
                'hl.fragsize': 300,
                'rows': 300,})
        
        self.assertEqual(len(results),300) 
        
    def test_solr_return_500(self):
        solr = pysolr.Solr('http://localhost:8983/solr/keyword')
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_files = root+'/python/data/image_json.json'
        
        with open(path_to_files) as data_file:    
            data = json.load(data_file)
        
        solr.add(data)
        
        results = solr.search("Belfast", **{
                'hl': 'true',
                'hl.fragsize': 500,
                'rows': 500,})
        
        self.assertEqual(len(results),500) 
    
    def test_keyword(self):
        solr = pysolr.Solr('http://localhost:8983/solr/unittest')
        solr.add([{
               "id": "Belfast",
               "description": "This is about Belfast",
               },
              {
               "id": "Lisburn",
               "description": "This is about Lisburn",
               },
               {
               "id": "Titanic",
               "description": "This is about Titanic",
               },]) 
    
        query_generic = solr.search("about")
        query_titanic = solr.search("Titanic")
        generic_result_list = []
        titanic_result_list = []
        generic_test = ['Belfast','Lisburn','Titanic']
        titanic_test = ['Titanic']
    
    
        for result in query_titanic:
            titanic_result_list.append(result['id'])
        
        for result in query_generic:
            generic_result_list.append(result['id'])
        
        self.assertEqual(generic_result_list,generic_test)
        self.assertEqual(titanic_result_list,titanic_test)
   
    def test_correct_server_request(self):
        response = requests.get('http://localhost:5000/hello')
        
        self.assertEqual(response.status_code, 200)
    
    def test_wrong_server_request(self):
        response = requests.get('http://localhost:5000/randomdoesntexist')
        
        self.assertEqual(response.status_code, 404)
        
    def test_server_json_response(self):
        response = requests.get("http://localhost:5000/python/solr/?tag=Titanic")
        test_response = '[{"lat": "None", "lon": "None", "id": "https://farm9.staticflickr.com/8671/15769063172_7644c64cc7_b.jpg"}, {"lat": "54.608173", "lon": "-5.910097", "id": "https://farm1.staticflickr.com/583/20788008898_a3e514133d_b.jpg"}, {"lat": "54.608173", "lon": "-5.910097", "id": "https://farm1.staticflickr.com/661/20984319721_ee8f7c448d_b.jpg"}, {"lat": "54.606153", "lon": "-5.911695", "id": "https://farm4.staticflickr.com/3923/14923363887_84c257a706_b.jpg"}, {"lat": "54.607048", "lon": "-5.917339", "id": "https://farm2.staticflickr.com/1704/24192795369_97369f9a71_b.jpg"}]'
        json_response = json.loads(response.text)
        test_json = json.loads(test_response)
        self.assertEqual(test_json, json_response)
        
    def test_json_exists(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.assertTrue(os.path.exists(root+'/python/data/image_json.json'))
    
    def test_json_structure(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_files = root+'/python/data/image_json.json'
        
        with open(path_to_files) as data_file:      
            data = json.load(data_file)
            
            
        schema = {"type":"array",
                  "properties":{
                                "url":{"type":"string"},
                                "lat":{"type":["string","number"]},
                                "lon":{"type":["string","number"]},
                                "id":{"type":"string"},
                                "description":{"type":"array",
                                               "items":{
                                                        "type":"array",
                                                        "items":[{"type":"string"}]
                                                        }}
                                }
                  }
        
        test = validictory.validate(data, schema)
        self.assertEqual(test, None)
    
if __name__ =='__main__':
    unittest.main()