import ccm_db_api as api

key = 'GdYKPPiRPZ1xFq7D7JFng7PSlkIuWyGk9GDjXfcl'
guldgruvan = api.Guldgruvan(key)

df = guldgruvan.datasets('mj_yearly_metrics_labeled')
print(df)

# plt.plot(df['date'], df['close'])
# plt.show()
