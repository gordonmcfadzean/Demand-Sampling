import pandas as pd

df__ev_10m = pd.read_csv('C:\\Users\\mcfadzeang\\Desktop\\Ideas\\ADMD Predictor\\CLNR data for sampling approach\\tc6_power_chp_sorted.csv')

df__ev_10m['timestamp'] = pd.to_datetime(df__ev_10m['timestamp'], infer_datetime_format=True)

df__ev_10m = df__ev_10m.set_index(pd.DatetimeIndex(df__ev_10m['timestamp']))

df__ev_30m = df__ev_10m.resample('30min').mean()

df__ev_30m.to_csv('30min.csv')