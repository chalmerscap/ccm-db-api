import pandas as pd
import mysql.connector
import requests
import json
from pandas.io.json import json_normalize


class Guldgruvan:

    def __init__(self, key):
        self.key = key
        self.params = {'x-api-key': key}
        self.url_base = 'https://rn2ss6e8eb.execute-api.eu-west-3.amazonaws.com/alpha/'


    # Returns dataframe of all available instruments in Guldgruvan
    def instruments(self, print_json=False):
        endpoint = 'instruments'
        content = requests.get(self.url_base + endpoint, headers=self.params)
        print(content.url)
        if print_json:
            self.print_json(content['body'])

        try:
            return pd.DataFrame(json.loads(content['body']))
        except:
            print('error')


    def dailyprices(self, instrument, first, last, print_json=False):
        endpoint = 'dailyprices'
        content = requests.get(self.url_base + endpoint, headers=self.params, params = {'instrument': instrument, 'first': first, 'last': last}).json()
        if print_json:
            print(content['body'])

        try:
            return pd.DataFrame(json.loads(content['body']))
        except:
            print('error')
 
    
    def print_json(self, content):
        print(json.dumps(content, indent=4, sort_keys=True))
