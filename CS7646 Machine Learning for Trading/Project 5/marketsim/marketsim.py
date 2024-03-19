""""""  		  	   		 	   			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
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
  		  	   		 	   			  		 			     			  	 
Student Name: Omkar Vaidya (replace with your name)  		  	   		 	   			  		 			     			  	 
GT User ID: ovaidya3 (replace with your User ID)  		  	   		 	   			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		 	   			  		 			     			  	 
"""  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import datetime as dt  		  	   		 	   			  		 			     			  	 
import os  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import numpy as np  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
import pandas as pd  		  	   		 	   			  		 			     			  	 
from util import get_data, plot_data
  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
def compute_portvals(  		  	   		 	   			  		 			     			  	 
    orders_file="./orders/orders.csv",  		  	   		 	   			  		 			     			  	 
    start_val=1000000,  		  	   		 	   			  		 			     			  	 
    commission=9.95,  		  	   		 	   			  		 			     			  	 
    impact=0.005,  		  	   		 	   			  		 			     			  	 
):  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Computes the portfolio values.  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		 	   			  		 			     			  	 
    :type orders_file: str or file object  		  	   		 	   			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		 	   			  		 			     			  	 
    :type start_val: int  		  	   		 	   			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		 	   			  		 			     			  	 
    :type commission: float  		  	   		 	   			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		 	   			  		 			     			  	 
    :type impact: float  		  	   		 	   			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		 	   			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    # this is the function the autograder will call to test your code  		  	   		 	   			  		 			     			  	 
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		 	   			  		 			     			  	 
    # code should work correctly with either input  		  	   		 	   			  		 			     			  	 
    # TODO: Your code here
    from collections import defaultdict

    orders = pd.read_csv(orders_file)
    orders['Date'] = pd.to_datetime(orders['Date'])

    stock_list = list(orders["Symbol"].unique())

    start_date = orders.at[0, 'Date']
    end_date = orders['Date'].iloc[-1]

    stock_prices = get_data(stock_list, pd.date_range(start_date, end_date))
    stock_prices = stock_prices[stock_list]
    stock_prices_df = pd.DataFrame(index=stock_prices.index, data=stock_prices.values)
    stock_prices_df.columns = stock_list

    curr_portfolio = defaultdict(float)
    cash_portfolio = defaultdict(float)
    cash_portfolio['Cash'] = start_val

    # column_names = ['Value']
    output = pd.DataFrame(index = stock_prices_df.index)

    for row in stock_prices_df.itertuples():

        for row_order in orders[orders['Date'] == row.Index].itertuples():

            if row_order.Order == 'BUY':
                buy_sell = 1
            else:
                buy_sell = -1

            curr_portfolio[row_order.Symbol] += row_order.Shares * buy_sell
            cash_val = row_order.Shares * getattr(row, row_order.Symbol) * -1 * buy_sell
            impact_val = abs(cash_val) * impact
            cash_portfolio['Cash'] += cash_val - impact_val - commission

        for stock in curr_portfolio.keys():
            cash_portfolio[stock] = curr_portfolio[stock] * getattr(row, stock)
        output.loc[row.Index, 0] = sum(cash_portfolio.values())

    return output
  		  	   		 	   			  		 			     			  	 


def author():
    return 'ovaidya3'
  		  	   		 	   			  		 			     			  	 
def test_code():  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    Helper function to test code  		  	   		 	   			  		 			     			  	 
    """  		  	   		 	   			  		 			     			  	 
    # this is a helper function you can use to test your code  		  	   		 	   			  		 			     			  	 
    # note that during autograding his function will not be called.  		  	   		 	   			  		 			     			  	 
    # Define input parameters  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    of = "./orders/orders-01.csv"
    sv = 1000000  		  	   		 	   			  		 			     			  	 
  		  	   		 	   			  		 			     			  	 
    # Process orders  		  	   		 	   			  		 			     			  	 
    portvals = compute_portvals(orders_file=of, start_val=sv)
    print(portvals)
    if isinstance(portvals, pd.DataFrame):  		  	   		 	   			  		 			     			  	 
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		 	   			  		 			     			  	 
    else:  		  	   		 	   			  		 			     			  	 
        "warning, code did not return a DataFrame"  		  	   		 	   			  		 			     			  	 


    def author():
        return 'ovaidya3'

if __name__ == "__main__":  		  	   		 	   			  		 			     			  	 
    test_code()  		  	   		 	   			  		 			     			  	 
