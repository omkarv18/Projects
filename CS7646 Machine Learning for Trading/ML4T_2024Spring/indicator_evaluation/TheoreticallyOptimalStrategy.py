import numpy as np
import pandas as pd
import datetime as dt
from util import get_data, plot_data



def author(self):
    return 'ovaidya3'

def testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):

    stock = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="Adj Close")
    stock.drop('SPY', axis=1, inplace=True)

    returns = stock.diff()

    positive_returns = returns[symbol] > 0
    returns['position'] = np.where(positive_returns, 1000, -1000)
    returns['position'].iat[0] = 0

    returns[symbol] = returns['position'].diff()

    returns[symbol] = returns[symbol].shift(-1, fill_value=0)

    return returns[[symbol]]

df_trades = testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)

# print(df_trades)
    