import ccm_db_api as api
import matplotlib.pyplot as plt

key = ''
guldgruvan = api.Guldgruvan(key)

# df = guldgruvan.prices_daily('AAK.ST', '2018-01-01', '2018-02-01', print_json=0)
# df = guldgruvan.report_year('AAK.ST', '2018', print_json=0)
df = guldgruvan.instruments(print_json=0)
print(df)

# plt.plot(df['date'], df['close'])
# plt.show()
