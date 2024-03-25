import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IntegrationRules import integration_tol, simpsons

def cum_dist_normal(t):
    z = abs(t)

    y = 1 / (1 + 0.2316419 * z)
    a1 = 0.319381530
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429

    m = 1 - (np.exp((-t**2) / 2) * ((a1 * y) + (a2 * (y **2)) + (a3 * (y**3)) + (a4 * (y**4)) + (a5 * (y**5)))) / (np.sqrt(2 * np.pi))

    if t > 0:
        nn = m
    else:
        nn = 1 - m
    return nn

def black_scholes(t, S, K, T, sigma, r, q, position):

    d1 = (np.log(S/K) + (r - q + ((sigma ** 2) / 2)) * (T - t)) / (sigma * np.sqrt(T - t))
    d2 = d1 - sigma * np.sqrt(T - t)

    if position == 'd1d2':
        return d1, d2, np.vectorize(cum_dist_normal)(d1), np.vectorize(cum_dist_normal)(d2)

    if position == 'C':
        C = S * np.exp(-q * (T - t)) * np.vectorize(cum_dist_normal)(d1) - K * np.exp(-r * (T - t)) * np.vectorize(cum_dist_normal)(d2)
        return C
    
    if position == 'P':
        P = K * np.exp(-r * (T - t)) * np.vectorize(cum_dist_normal)(-d2) - S * np.exp(-q * (T - t)) * np.vectorize(cum_dist_normal)(-d1)
        return P

    if position == 'delta_C':
        delta_C = np.exp(-q * (T - t)) * np.vectorize(cum_dist_normal)(d1)
        return delta_C

    if position == 'delta_P':
        delta_P = -np.exp(-q * (T - t)) * np.vectorize(cum_dist_normal)(-d1)
        return delta_P

def hedge_portfolio(t, S, K, T, sigma, r, q, delta_T, calc_num, put=0, call=0, shares=0, cash=0):
    # S = list of share prices
    # delta_T = time to next calculation - weekly = 1/52
    # r = continuously compounding annualized risk free rate
    # number of calculations
    # put = number of put options

    column_names = ['Put Options BH', 'Call Options BH', 'Asset Position BH', 'Cash Position BH', 'Put Options AH', 'Call Options AH', 'Asset Position AH', 'Cash Position AH']
    df = pd.DataFrame(columns=column_names)

    curr_shares = shares
    curr_put = put
    curr_call = call
    curr_cash = cash

    curr_position = {'Put Options BH': curr_put, 'Call Options BH': curr_call, 'Asset Position BH': curr_shares, 'Cash Position BH': curr_cash, 'Put Options AH': curr_put, 'Call Options AH': curr_call, 'Asset Position AH': 0, 'Cash Position AH': 0}

    for i in range(calc_num):
        
        curr_cash = curr_cash * np.exp(r * delta_T * int(i > 0))
        curr_position['Cash Position BH'] = curr_cash
        curr_position['Asset Position BH'] = curr_shares

        delta_port = curr_call * black_scholes(t+(i * delta_T), S[i], K, T, sigma, r, q, position='delta_C') + curr_put * black_scholes(t+(i * delta_T), S[i], K, T, sigma, r, q, position='delta_P') + curr_shares
        print(delta_port)
        print(black_scholes(t+(i * delta_T), S[i], K, T, sigma, r, q, position='delta_P'))

        curr_shares -= delta_port
        curr_cash += delta_port * S[i]

        curr_position['Cash Position AH'] = curr_cash
        curr_position['Asset Position AH'] = curr_shares
        

        df.loc[i] = curr_position

    return df

def Normal_dist(z):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-z**2 / 2)



# print(cum_dist_normal(1))

# C = black_scholes(t=0, S=40, K=40, T=0.25, sigma=0.2, q=0.01, r=0.05, position='C')

# print(C)

# S_vals = np.arange(0, 100)

# d1, d2, C, P = black_scholes(t=0, S=S_vals, K=40, T=0.5, sigma=0.3, q=0, r=0.05)



# P_new = P - (40 - S_vals)

# print(P_new)

# plt.plot(S_vals, P_new)
# plt.show()

# d1, d2 = black_scholes(t=0, S=40, K=40, T=0.25, sigma=0.2, q=0.01, r=0.05, position='d1d2')

# t = 0
# S = 40
# K=40
# T=0.25
# sigma=0.2
# q=0.01
# r=0.05

# C = S * np.exp(-q * (T - t)) * np.vectorize(integration_tol)(simpsons, Normal_dist, -10, d1, tol=1e-12) - K * np.exp(-r * (T - t)) * np.vectorize(integration_tol)(simpsons, Normal_dist, -10, d2, tol=1e-12)

# d1, d2, nd1, nd2 = black_scholes(t=0, S=50, K=45, T=5/12, sigma=0.3, q=0.01, r = 0.03, position='d1d2')

# print(d1, nd1)

# delta_c= black_scholes(t=0, S=50, K=45, T=5/12, sigma=0.3, q=0.01, r = 0.03, position='delta_C')

# print(delta_c)

# d1, d2, nd1, nd2 = black_scholes(t=0, S=50, K=45, T=5/12, sigma=0.3, q=0.01, r = 0.03, position='d1d2')

# print(d2, nd2)

t = 0
S = [25, 30, 26, 22, 27]
K = 30
T = 0.25
sigma = 0.3
r = 0.02
q = 0
delta_T = 1/52
calc_num = 5
put = 1000
shares = 400
cash = 10000

new_df = hedge_portfolio(t, S, K, T, sigma, r, q, delta_T, calc_num, put=put, call=0, shares=shares, cash=cash)

print(new_df)

# print(black_scholes(t, S[0], K, T, sigma, r, q, position='delta_P'))