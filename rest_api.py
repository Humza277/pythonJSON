# CRUD Create red update delete

from dict_keys import flux

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req)


# class Di:
#     def __init__(self, post_codes_req):
#         self.post_codes_req = post_codes_req


# Di.__init__()

# Exercise is to fetch data by key value pairs within dictionaries
# Create a function to return the above vaues (Key:value)
# Create a class and move the code inside the class
