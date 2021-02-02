import os
# import warnings
#
# warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import jsonify
import warnings
warnings.filterwarnings('ignore')
from statsmodels.tsa.arima_model import ARIMA, ARIMA_DEPRECATION_WARN
# warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
#                         FutureWarning)
# warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
#                         FutureWarning)
#
# warnings.warn(ARIMA_DEPRECATION_WARN, FutureWarning)

from backend.selling import service, serializer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
# from pandas import datetime
from sklearn.metrics import mean_squared_error

from backend.selling.repository import get_quote_closes_values
import json
filtered_quotes = service.get_filtered_quotes(3)
json=json.dumps(serializer.convert_quotes_to_dict(filtered_quotes))
df =pd.read_json(json)

df.head(5)
# df['dateTime']=pd.to_datetime(df['dateTime'], format='%Y-%m-%d %H:%M:%S')
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
# data = pd.read_csv('trade/csv/2.csv',sep=',').fillna(0)

# data = pd.read_csv('trade/csv/1.csv', sep=',', parse_dates=['Date'], date_parser=dateparse).fillna(0).r
# df.set_index('dateTime')
plt.figure()
lag_plot(df['close'], lag=3)
plt.title('TESLA Stock - Autocorrelation plot with lag = 3')
plt.show()
plt.figure(figsize=(12, 5), dpi=100)
plt.autoscale(axis='x', tight=True)
plt.plot(df["dateTime"], df["close"])
# plt.xticks(np.arange(0,1259, 200), df['dateTime'][0:1259:200])
plt.title("TESLA stock price over time")
plt.xlabel("time")
plt.ylabel("price")
plt.show()

train_data, test_data = df[0:int(len(df)*0.7)], df[int(len(df)*0.7):]
training_data = train_data['close'].values
test_data = test_data['close'].values
history = [x for x in training_data]
model_predictions = []
N_test_observations = len(test_data)
for time_point in range(N_test_observations):
    model = ARIMA(history, order=(4,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    model_predictions.append(yhat)
    true_test_value = test_data[time_point]
    history.append(true_test_value)
    # print(len(test_data))
    # print(len(model_predictions))
MSE_error = mean_squared_error(test_data, model_predictions)
print('Testing Mean Squared Error is {}'.format(MSE_error))
test_set_range = df[int(len(df)*0.7):].index
plt.plot(test_set_range, model_predictions, color='blue', marker='o', linestyle='dashed',label='Predicted Price')
plt.plot(test_set_range, test_data, color='red', label='Actual Price')
plt.title('TESLA Prices Prediction')
plt.xlabel('Date')
plt.ylabel('Prices')
# plt.xticks(np.arange(881,1259,50), df.Date[881:1259:50])
plt.legend()
plt.show()
