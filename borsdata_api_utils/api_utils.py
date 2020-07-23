import os
import requests
import json
from pandas.io.json import json_normalize


key = '075f96b9d19e45d28c1f74a0756b52a5'
url_base = 'https://apiservice.borsdata.se/v1/'
params = {'authKey': key, 'maxYearCount': '20', 'maxcount': '20'}

# Returns dataframe of all available instruments in Börsdata API
def instruments():
    endpoint = 'instruments'
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['instruments'])

# Returns dataframe of yearly history for a certain ticker and kpi
def kpi_history(ticker_id, kpi_id):
    endpoint = 'instruments/{}/kpis/{}/{}/{}/history'.format(str(ticker_id), str(kpi_id) , 'year', 'mean')
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['values'])

# Returns dataframe of a certain kpi for all tickers
def kpi_all(kpi_id):
    endpoint = 'instruments/kpis/{}/{}/{}'.format(str(kpi_id), '1year', 'mean')
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['values'])

# Returns dataframe of historical daily stock prices for a certain ticker
def prices(ticker_id):
    endpoint = 'instruments/{}/stockprices'.format(str(ticker_id))
    content = requests.get(url_base + endpoint, params).json()
    
    return json_normalize(content['stockPricesList'])

# Returns dataframe of all reports for a certain ticker
def reports(ticker_id):
    endpoint = 'instruments/{}/reports'.format(str(ticker_id))
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['reportsYear'])


def report_meta():
    endpoint = 'instruments/reports/metadata'
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['reportMetadatas'])


def prices_last():
    endpoint = 'instruments/stockprices/last'
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['stockPricesList'])


def prices_date(date):
    endpoint = 'instruments/stockprices/date'
    params['date'] = date
    content = requests.get(url_base + endpoint, params).json()

    return json_normalize(content['stockPricesList'])


# Prints the output of requests.get() in a readable manner
def print_json(content):
    print(json.dumps(content, indent=4, sort_keys=True))


if __name__ == '__main__':
    x = prices_date('2020-05-01')

    print(x)