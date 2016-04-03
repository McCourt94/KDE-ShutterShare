import unittest
import JSONgenerate
import os
import json
from subprocess import Popen, PIPE, STDOUT

class MyTest(unittest.TestCase):
    def test_if_JSON_file_created(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        path_to_files = root+'/python/data/image_json.json'
        
        assert os.path.exists(path_to_files)
    
    def test_json_format(self):
        
        
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))       
        path_to_files = root+'/python/data/image_json.json'
        data = open(path_to_files,'r')
        actual_json_format = data.read()
        
        self.ass
        self.assertEqual(json,       
                    actual_json_format)
        
            


if __name__ == '__main__':
    unittest.main()