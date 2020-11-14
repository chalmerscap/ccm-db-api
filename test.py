import ccm_db_api as api
import matplotlib.pyplot as plt

key = ''
guldgruvan = api.Guldgruvan(key)

df = guldgruvan.dailyprices('ABB.ST', '2011-02-11', '2014-12-14', print_json=False)
# df = api.instruments(print_json=True)
print(df)

# plt.plot(df['date'], df['close'])
# plt.show()