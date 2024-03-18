import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from TheoreticallyOptimalStrategy import testPolicy
from marketsimcode import compute_portvals
from util import get_data


def author():
    return 'ovaidya3'

def rsi(port_vals, window=14):
    def avg_gain(values, window=14):
        sum = values[values > 0].sum()
        mean = sum / window
        return mean

    def avg_loss(values, window=14):
        sum = values[values < 0].sum()
        mean = sum / window
        return mean

    returns = port_vals.pct_change().dropna()

    cols = ['avg_gain', 'avg_loss', 'RSI']
    results = pd.DataFrame(columns=cols)
    results['avg_gain'] = returns[port_vals.columns[0]].rolling(window=14).apply(avg_gain, raw=True)
    results['avg_loss'] = abs(returns[port_vals.columns[0]].rolling(window=14).apply(avg_loss, raw=True))

    results['RSI'] = 100 - (100 / (1 + (results['avg_gain'] / results['avg_loss'])))
    results[port_vals.columns[0]] = port_vals[port_vals.columns[0]]
    results['Overbought'] = 70
    results['Oversold'] = 30
    return results


def bollinger(port_vals, window=14):

    cols = [port_vals.columns[0], 'sma', 'std', 'upper', 'lower', 'bollinger', "BBP"]
    results = pd.DataFrame(columns=cols)


    results['sma'] = port_vals[port_vals.columns[0]].rolling(window=window).mean()
    results['std'] = port_vals[port_vals.columns[0]].rolling(window=window).std()
    results['bollinger'] = (port_vals[port_vals.columns[0]] - results['sma']) / (2 * results['std'])
    results['upper'] = results['sma'] + 2 * results['std']
    results['lower'] = results['sma'] - 2 * results['std']
    results['BBP'] = (port_vals[port_vals.columns[0]] - (results['lower'])) / (results['upper']-results['lower'])
    results[port_vals.columns[0]] = port_vals[port_vals.columns[0]].copy()
    results['1'] = 1
    results['-1'] = -1

    return results

def stochastic(port_vals, kwindow=14, dwindow=3):

    cols = [port_vals.columns[0], 'max', 'min', '%k', '%d']
    results = pd.DataFrame(columns=cols)

    results[port_vals.columns[0]] = port_vals[port_vals.columns[0]].copy()
    results['max'] = port_vals[port_vals.columns[0]].rolling(window=kwindow).max()
    results['min'] = port_vals[port_vals.columns[0]].rolling(window=kwindow).min()
    results['%k'] = (results[port_vals.columns[0]] - results['min']) / (results['max'] - results['min']) * 100

    results['%d'] = round(results['%k'].rolling(window=dwindow).mean(), 6)

    return results

def money_flow(port_vals, high, low, volume):
    def positive_flow(values, window=14):
        sum = values[values > 0].sum()
        return sum
    def negative_flow(values, window=14):
        sum = values[values < 0].sum()
        return sum

    cols = [port_vals.columns[0], 'High', 'Low', 'Volume', 'Typical']
    results = pd.DataFrame(columns=cols)

    results[port_vals.columns[0]] = port_vals[port_vals.columns[0]]
    results['High'] = high[port_vals.columns[0]]
    results['Low'] = low[port_vals.columns[0]]
    results['Volume'] = volume[port_vals.columns[0]]
    results['Typical'] = (results['High'] + results['Low'] + results[port_vals.columns[0]]) / 3
    results['raw_money_flow'] = results['Volume'] * results['Typical'] * np.sign(results['Typical'].diff())
    results['pos_money_flow_sum'] = results['raw_money_flow'].rolling(window=14).apply(positive_flow, raw=True)
    results['neg_money_flow_sum'] = results['raw_money_flow'].rolling(window=14).apply(negative_flow, raw=True)
    results['money_flow_ratio'] = abs(results['pos_money_flow_sum'] / results['neg_money_flow_sum'])
    results['money_flow_index'] = 100 - (100 / (1 + results['money_flow_ratio']))
    results['Overbought'] = 80
    results['Oversold'] = 20

    return results

def CCI(port_vals, high, low, volume, window=20):

    cols = [port_vals.columns[0], 'High', 'Low', 'Volume', 'Typical']
    results = pd.DataFrame(columns=cols)

    results[port_vals.columns[0]] = port_vals[port_vals.columns[0]]
    results['High'] = high[port_vals.columns[0]]
    results['Low'] = low[port_vals.columns[0]]
    results['Volume'] = volume[port_vals.columns[0]]
    results['Typical'] = (results['High'] + results['Low'] + results[port_vals.columns[0]]) / 3

    results['sma'] = results['Typical'].rolling(window=window).mean()
    results['Typical-sma'] = results['Typical'] - results['sma']
    results['Mean Deviation'] = abs(results['Typical-sma']).rolling(window=window).mean()
    results['CCI'] = results['Typical-sma'] / (0.015 * results['Mean Deviation'])
    results['Overbought'] = 100
    results['Oversold'] = -100
    return results
