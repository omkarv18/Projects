import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from util import get_data
from indicators import rsi, bollinger, stochastic, money_flow, CCI
from TheoreticallyOptimalStrategy import testPolicy
from marketsimcode import compute_portvals
import numpy as np

def author():
    return 'ovaidya3'

def performance_metrics(portfolio_vals):
    returns = portfolio_vals.pct_change()

    standard_deviation = returns['Value'].std(skipna=True)
    mean = returns['Value'].mean(skipna=True)
    returns['Value'] += 1

    cumulative_returns = returns['Value'].prod(skipna=True) - 1

    return cumulative_returns, standard_deviation, mean

if __name__ == "__main__":

    # Part 1: Benchmark VS TOS Portfolio

    # Create TOS dataset
    df_trades = testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    portvals_tos = compute_portvals(df_trades, start_val=100000)
    portvals_tos['Value'] = portvals_tos['Value'] / portvals_tos['Value'].iat[0]

    # Create benchmark dataset
    benchmark = df_trades.copy()
    benchmark['JPM'] = 0
    benchmark['JPM'].iat[0] = 1000
    portvals_benchmark = compute_portvals(benchmark, start_val=100000)
    portvals_benchmark['Value'] = portvals_benchmark['Value'] / portvals_benchmark['Value'].iat[0]

    plt.figure(1)
    plt.plot(portvals_benchmark['Value'], color='purple')
    plt.plot(portvals_tos['Value'], color='red')
    plt.legend(["Benchmark", "TOS Portfolio"])
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.title("TOS Portfolio vs Benchmark Portfolio")
    plt.gcf().autofmt_xdate()
    plt.savefig("Part_1.png")
    plt.close()

    # Create Table
    cols = ['Cumulative Returns', 'Standard Deviation', 'Mean']
    performance_vals = pd.DataFrame(columns=cols)
    performance_vals.loc['TOS Portfolio'] = performance_metrics(portvals_tos)
    performance_vals.loc['Benchmark Portfolio'] = performance_metrics(portvals_benchmark)
    performance_vals.to_csv('Part_1_metrics.csv', index=True)

    # Part 2: Indicator Graphs

    symbol = "JPM"
    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)

    stock = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="Adj Close").drop(columns=["SPY"])
    High = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="High").drop(columns=["SPY"])
    Low = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="Low").drop(columns=["SPY"])
    Volume = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="Volume").drop(columns=["SPY"])
    Close = get_data([symbol], pd.date_range(sd, ed), addSPY=True, colname="Close").drop(columns=["SPY"])

    # Relative Strength Index (RSI) Plot

    rsi_val = rsi(stock)

    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True, num=2)

    axs[0].plot(rsi_val['RSI'], color='blue')
    axs[0].plot(rsi_val['Overbought'], color='red')
    axs[0].plot(rsi_val['Oversold'], color='red')
    axs[0].legend(["RSI", 'Overbought', 'Oversold'])
    axs[0].set_ylabel("RSI")
    axs[0].set_title("RSI Indicator on JPM stock")

    axs[1].plot(rsi_val[symbol], color='purple')
    axs[1].legend([symbol])
    axs[1].set_ylabel("Adjusted Stock Price")
    axs[1].set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Part_2_1.png")

    # Bollinger Bands Plot

    bollinger_val = bollinger(stock)

    fig2, axs2 = plt.subplots(2, 1, figsize=(10, 8), sharex=True, num=3)

    axs2[0].plot(bollinger_val[symbol], color='blue')
    axs2[0].plot(bollinger_val['sma'], color='purple')
    axs2[0].plot(bollinger_val['upper'], color='red')
    axs2[0].plot(bollinger_val['lower'], color='red')
    axs2[0].legend(["JPM", 'SMA', 'Upper Band', 'Lower Band'])
    axs2[0].set_ylabel("Stock Price")
    axs2[0].set_title("Bollinger Bands on JPM stock")

    axs2[1].plot(bollinger_val['bollinger'], color='purple')
    axs2[1].plot(bollinger_val['BBP'], color='blue')
    axs2[1].plot(bollinger_val['1'], color='red')
    axs2[1].plot(bollinger_val['-1'], color='red')
    axs2[1].legend(['Bollinger Indicator', 'BBP (or %B)'])
    axs2[1].set_ylabel("Indicator level")
    axs2[1].set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Part_2_2.png")

    # Stochastic Indicator

    stochastic_val = stochastic(stock, 14, 3)

    fig3, axs3 = plt.subplots(2, 1, figsize=(15, 12), sharex=True, num=4)

    axs3[0].plot(stochastic_val[symbol], color='blue')
    axs3[0].legend(["JPM"])
    axs3[0].set_ylabel("Stock Price")
    axs3[0].set_title('Stochastic Indicator on JPM Stock')

    axs3[1].plot(stochastic_val['%k'], color='green')
    axs3[1].plot(stochastic_val['%d'], color='purple')
    axs3[1].legend(['%K', '%D'])
    axs3[1].set_ylabel("Indicator level")
    axs3[1].set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Part_2_3.png")

    # Money Flow Index

    money_flow_val = money_flow(Close, High, Low, Volume)

    fig4, axs4 = plt.subplots(2, 1, figsize=(15, 12), sharex=True, num=5)

    axs4[0].plot(money_flow_val[symbol], color='blue')
    axs4[0].legend(["JPM"])
    axs4[0].set_ylabel("Stock Price")
    axs4[0].set_title('Money Flow Indicator on JPM Stock')

    axs4[1].plot(money_flow_val['money_flow_index'], color='green')
    axs4[1].plot(money_flow_val['Overbought'], color='red')
    axs4[1].plot(money_flow_val['Oversold'], color='red')
    axs4[1].legend(['Money Flow Index', 'Overbought', 'Oversold'])
    axs4[1].set_ylabel("Indicator level")
    axs4[1].set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Part_2_4.png")

    # Commodity Channel Index (CCI)

    CCI_val = CCI(Close, High, Low, Volume, window=20)

    fig5, axs5 = plt.subplots(2, 1, figsize=(15, 12), sharex=True, num=6)

    axs5[0].plot(CCI_val[symbol], color='blue')
    axs5[0].legend(["JPM"])
    axs5[0].set_ylabel("Stock Price")
    axs5[0].set_title('Commodity Channel Index Indicator on JPM Stock')

    axs5[1].plot(CCI_val['CCI'], color='green')
    axs5[1].plot(CCI_val['Overbought'], color='red')
    axs5[1].plot(CCI_val['Oversold'], color='red')
    axs5[1].legend(['CCI'])
    axs5[1].set_ylabel("Indicator level")
    axs5[1].set_xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Part_2_5.png")