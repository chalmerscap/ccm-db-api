import ccm_db_api as api
import matplotlib.pyplot as plt

key = ''
guldgruvan = api.Guldgruvan(key)

df = guldgruvan.dailyprices('AAK.ST', '2018-02-11', '2020-11-15', print_json=False)
# df = guldgruvan.instruments(print_json=True)
print(df)

# plt.plot(df['date'], df['close'])
# plt.show()