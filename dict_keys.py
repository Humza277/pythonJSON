import requests
import json
import unittest
import math
from exercise_calc import Functions
import pytest


type_json = requests.get("https://api.postcodes.io/postcodes/se120nb")

post_code_json = type_json.json()

# def flux(self):
#     json_data = json.load(self)
#     data = json_data.json()
#     for key in data:
#         print(key, data[key])

# recursive class, calls it self
class Dictreader:
    def get_all_values(self, post_code_json):
        for key, value in post_code_json.items():
            if type(value) is dict:
                self.get_all_values(value)
            else:
                print(key, ":", value)


dict_reader = Dictreader()
dict_reader.get_all_values(post_code_json)


# functions to test
class Functions:

    def find_sqrt(self, num):
        return math.sqrt(num)
    def find_ceil(self, num):
        return math.ceil(num)

# test for the above methods
class Calc_Test(unittest.TestCase):
    a = Functions()
    def test_sqrt(self):
        self.assertEqual(self.a.find_sqrt(16), 4)
    def test_find_ceil(self):
        self.assertEqual(self.a.find_ceil(25.8237), 26)

