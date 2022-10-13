import os
import requests
import json
from pandas.io.json import json_normalize


class Borsdata:

    def __init__(self, key):
        self.key = key
        self.params = {'authKey': key, 'maxYearCount': '20', 'maxcount': '20'}
        self.url_base = 'https://apiservice.borsdata.se/v1/'


    
    def instruments(self, print=False):
        '''
        Returns dataframe of all available instruments in Börsdata API
        '''
        endpoint = 'instruments'
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['instruments'])


    def kpi_history(self, ticker_id, kpi_id, print=False):
        '''
        Returns dataframe of yearly history for a certain ticker and kpi
        '''
        endpoint = 'instruments/{}/kpis/{}/{}/{}/history'.format(str(ticker_id), str(kpi_id) , 'year', 'mean')
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['values'])


    def kpi_all(self, kpi_id, print=False):
        '''
        Returns dataframe of a certain kpi for all tickers
        '''
        endpoint = 'instruments/kpis/{}/{}/{}'.format(str(kpi_id), '1year', 'mean')
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['values'])


    def prices(self, ticker_id, print=False):
        '''
        Returns dataframe of historical daily stock prices for a certain ticker
        '''
        endpoint = 'instruments/{}/stockprices'.format(str(ticker_id))
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)
        
        return json_normalize(content['stockPricesList'])


    def reports(self, ticker_id, print=False):
        '''
        Returns dataframe of all reports for a certain ticker
        '''
        endpoint = 'instruments/{}/reports'.format(str(ticker_id))
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['reportsYear'])


    def report_meta(self, print=False):
        endpoint = 'instruments/reports/metadata'
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['reportMetadatas'])


    def prices_last(self, print=False):
        endpoint = 'instruments/stockprices/last'
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['stockPricesList'])


    def prices_date(self, date, print=False):
        endpoint = 'instruments/stockprices/date'
        self.params['date'] = date
        content = requests.get(self.url_base + endpoint, self.params).json()
        if print:
            self.print_json(content)

        return json_normalize(content['stockPricesList'])


    # Prints the output of requests.get() in a readable manner dfd
    def print_json(self, content):
        print(json.dumps(content, indent=4, sort_keys=True))
