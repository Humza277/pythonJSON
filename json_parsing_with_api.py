import requests
import json_api

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.content)
print(type(post_codes_req.content))
print(post_codes_req.headers)
print(post_codes_req)


# class Check():
#     def __init__(self):
#         json_api.check_status(self)
#
#
# Check.__init__(post_codes_req)




