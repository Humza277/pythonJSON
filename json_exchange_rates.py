#import jason module
import json


# create class exchange rates
# with attributes
# fetch data from .json file
# display data
# display type data
# display rate with curremcys

class Exchange_Rates:
    #inits the method
    def __init__(self):
        # command to read the file
        with open("exchange_rates.json", "r") as exchange_files:
            # loads the json data in the data variable
            data = json.load(exchange_files)
            # iterates through the file
            for e in data:
                if e == 'rates':
                    # prints the output
                    print(data['rates'])
                    #print(data)

            #print(data)


e = Exchange_Rates
e.__init__(Exchange_Rates)
