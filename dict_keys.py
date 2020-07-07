import requests
import json

type_json = requests.get("https://api.postcodes.io/postcodes/se120nb")

post_code_json = type_json.json()

# def flux(self):
#     json_data = json.load(self)
#     data = json_data.json()
#     for key in data:
#         print(key, data[key])


class JSONReader:
    def get_all_values(self, post_code_json):
        for key, value in post_code_json.items():
            if type(value) is dict:
                self.get_all_values(value)
            else:
                print(key, ":", value)


json_reader = JSONReader()
json_reader.get_all_values(post_code_json)
