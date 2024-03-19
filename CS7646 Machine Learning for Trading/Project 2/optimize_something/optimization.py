""""""  		  	   		 	   			  		 			     			  	 
"""MC1-P2: Optimize a portfolio.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		 	   			  		 			     			  	 
All Rights Reserved  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Template code for CS 4646/7646  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			     			  	 
or edited.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			     			  	 
GT honor code violation.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
-----do not edit anything above this line---  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
Student Name: Omkar Kiran Vaidya  		  	   		 	   			  		 			     			  	 
GT User ID: ovaidya3 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 903867937 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import datetime as dt
import os
  		  	   		 	   			  		 			     			  	 
import numpy as np  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import matplotlib.pyplot as plt  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
from util import get_data, plot_data  		  	   		 	   			  		 			     			  	 
from scipy.optimize import minimize
  		  	   		 	   			  		 			     			  	 
# This is the function that will be tested by the autograder  		  	   		 	   			  		 			     			  	 
# The student must update this code to properly implement the functionality  		  	   		 	   			  		 			     			  	 
def optimize_portfolio(  		  	   		 	   			  		 			     			  	 
    sd=dt.datetime(2008, 1, 1),
    ed=dt.datetime(2009, 1, 1),
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   			  		 			     			  	 
    gen_plot=False,  		  	   		 	   			  		 			     			  	 
):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	   			  		 			     			  	 
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	   			  		 			     			  	 
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	   			  		 			     			  	 
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	   			  		 			     			  	 
    statistics.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			     			  	 
    :type sd: datetime  		  	   		 	   			  		 			     			  	 
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			     			  	 
    :type ed: datetime  		  	   		 	   			  		 			     			  	 
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	   			  		 			     			  	 
        symbol in the data directory)  		  	   		 	   			  		 			     			  	 
    :type syms: list  		  	   		 	   			  		 			     			  	 
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   			  		 			     			  	 
        code with gen_plot = False.  		  	   		 	   			  		 			     			  	 
    :type gen_plot: bool  		  	   		 	   			  		 			     			  	 
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	   			  		 			     			  	 
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	   			  		 			     			  	 
    :rtype: tuple  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			     			  	 
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 	   			  		 			     			  	 
    prices = prices_all[syms]  # only portfolio symbols  		  	   		 	   			  		 			     			  	 
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # find the allocations for the optimal portfolio

    # note that the values here ARE NOT meant to be correct for a test case  		  	   		 	   			  		 			     			  	 
    # allocs = np.asarray(
    #     [0.2, 0.2, 0.3, 0.3])
    allocs = np.ones(len(syms)) / len(syms)
      # add code here to find the allocations

    def compute_daily_portfolio(prices, alloc):
        normed = prices.div(prices.iloc[0])
        alloced = normed * alloc[np.newaxis, :]
        port_val = alloced.sum(axis=1)
        return port_val

    def compute_daily_returns(df):
        daily_returns = (df / df.shift(1)) - 1
        daily_returns.iloc[0] = 0
        return daily_returns[1:]

    def cum_ret(df):
        return (df.iloc[-1] / df.iloc[0]) - 1

    def avg_daily_returns(df):
        return df.mean()

    def std_daily_returns(df):
        return df.std()

    def neg_sharpe_ratio(allocs, prices):
        daily_port_vals = compute_daily_portfolio(prices, allocs)
        daily_returns = compute_daily_returns(daily_port_vals)
        avg_daily_rets = avg_daily_returns(daily_returns)
        std_daily_rets = std_daily_returns(daily_returns)

        return -(avg_daily_rets / std_daily_rets) * np.sqrt(252)

    bounds = [(0, 1) for _ in range(len(allocs))]

    def constraint(allocs):
        return np.sum(allocs) - 1.0

    constraints = [{'type': 'eq', 'fun': constraint}]

    result = minimize(neg_sharpe_ratio, allocs, args=(prices, ), bounds = bounds, constraints=constraints, method='SLSQP', options={'disp': False})

    allocs = result.x.copy()

    portfolio_prices = compute_daily_portfolio(prices, allocs)

    cr = cum_ret(portfolio_prices)

    adr = avg_daily_returns(compute_daily_returns(portfolio_prices))

    sddr = std_daily_returns(compute_daily_returns(portfolio_prices))

    sr = -neg_sharpe_ratio(allocs, prices)

  		  	   		 	   			  		 			     			  	 
    # Get daily portfolio value  		  	   		 	   			  		 			     			  	 
    prices_SPY = prices_SPY / prices_SPY[0]  # add code here to compute daily portfolio values
  		  	   		 	   			  		 			     			  	 
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 	   			  		 			     			  	 
    if gen_plot:  		  	   		 	   			  		 			     			  	 
        # add code to plot here  		  	   		 	   			  		 			     			  	 
        df_temp = pd.concat(  		  	   		 	   			  		 			     			  	 
            [portfolio_prices, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )

        df_temp.plot(y=["Portfolio", "SPY"], title = "Portfolio vs SPY")
        plt.xlabel("Date")
        plt.ylabel("Normalized Price")
        plt.legend(["Portfolio", "SPY"])
        plt.savefig("Figure1.png")

  		  	   		 	   			  		 			     			  	 
    return (allocs, cr, adr, sddr, sr)
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    This function WILL NOT be called by the auto grader.  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    start_date = dt.datetime(2009, 6, 1)
    end_date = dt.datetime(2010, 6, 1)
    symbols = ["IBM", "X", "GLD", "JPM"]
  		  	   		 	   			  		 			     			  	 
    # Assess the portfolio  		  	   		 	   			  		 			     			  	 
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	   			  		 			     			  	 
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True
    )  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Print statistics  		  	   		 	   			  		 			     			  	 
    print(f"Start Date: {start_date}")  		  	   		 	   			  		 			     			  	 
    print(f"End Date: {end_date}")  		  	   		 	   			  		 			     			  	 
    print(f"Symbols: {symbols}")  		  	   		 	   			  		 			     			  	 
    print(f"Allocations:{allocations}")  		  	   		 	   			  		 			     			  	 
    print(f"Sharpe Ratio: {sr}")  		  	   		 	   			  		 			     			  	 
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	   			  		 			     			  	 
    print(f"Average Daily Return: {adr}")  		  	   		 	   			  		 			     			  	 
    print(f"Cumulative Return: {cr}")  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
if __name__ == "__main__":
    # This code WILL NOT be called by the auto grader  		  	   		 	   			  		 			     			  	 
    # Do not assume that it will be called  		  	   		 	   			  		 			     			  	 
    test_code()
