import ccm_db_api as api

key = ''
guldgruvan = api.Guldgruvan(key)

df = guldgruvan.instruments(print_json=True)
print(df)

