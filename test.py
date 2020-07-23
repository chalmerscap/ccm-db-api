import borsdata_api_utils as api_utils

key = ''
api = api_utils.Borsdata_api(key)

print(api.instruments())