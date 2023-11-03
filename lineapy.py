from lineapy import TimeSeries, ARIMA

data = [10, 12, 11, 15, 18, 17, 19, 25, 26, 27]
ts = TimeSeries.from_list(data)

arima = ARIMA()
arima.fit(ts)
forecast = arima.predict(steps=5)

print(forecast)
