#what is json, javascript object notation 
syntax JSON
used to send between a browser and a server

the data be text - string data\
hence json is written in json format 

- a string
- a number
- an object(json)
- an array
- a boolean
- null

where is the syntax derived from 
- data is stored in key value pairs 
{"name": "james", "age": "18"}
data is separated by a comma

Code block

    import json
    
    car_data = {"name": "tesla", "engine": "electronic "}
    print(car_data)
    
    print(type(car_data))
    
    car_data_json_string = json.dumps(car_data)
    print(type(car_data_json_string))
    
    with open("new_json_file.json", "w") as jsonfile:
        json.dump(car_data, jsonfile)
    
    with open("new_json_file.json") as jsonfile:
        car = json.load(jsonfile)
        print(type(car))
        print(car['name'])
        print(car['engine'])
