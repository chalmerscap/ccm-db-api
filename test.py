import ccm_db_api as api

key = '649de2c46ac74c20b2ba2708f4364c98'
guldgruvan = api.Guldgruvan(key)

df = guldgruvan.instruments(print_json=True)
print(df)

