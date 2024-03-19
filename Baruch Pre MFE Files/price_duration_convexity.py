#Code for computing price, duration, & Convexity of a bond given the yield of the bond

import numpy as np

def price_duration_convexity_yield(T, n, t_cash_flow, v_cash_flow, y):


    # T = bond maturity in months
    # n = number of cashflows
    # t_cash_flow = vector of cash flow dates (of size n)
    # v_cash_flow = vector of cash flows (of size n)
    # y = yield of bond

    B = 0 # price of bond
    D = 0 # duration of bond
    C = 0 # convexity of bond

    disc = np.empty(n)

    for i in range(n):
        disc[i] = np.exp(- t_cash_flow[i] * y)
        B = B + v_cash_flow[i] * disc[i]
        D = D + t_cash_flow[i] * v_cash_flow[i] * disc[i]
        C = C + (t_cash_flow[i] ** 2) * v_cash_flow[i] * disc[i]

    D = D / B 
    C = C / B

    return B, D, C


face_value = 100
coupon_rate = 0.04
T = 19
months = 6
y = 0.025

n = int(np.ceil(T / months)) # (T / months) & round up
t_cash_flow = [(T / 12.0) - ((months / 12.0) * j) for j in range(n)]
t_cash_flow = np.array(t_cash_flow[::-1].copy())
v_cash_flow = [(coupon_rate / (12 / months)) * face_value for _ in range(n-1)]
v_cash_flow.append((coupon_rate / (12 / months)) * face_value + face_value)

v_cash_flow = np.array(v_cash_flow.copy())


print(n)
print(t_cash_flow)
print(v_cash_flow)

answer = price_duration_convexity_yield(T, n, t_cash_flow, v_cash_flow, y)

print(f'Bond Price (B) = {answer[0]}, Bond Duration (D) = {answer[1]}, Bond Convexity (C) = {answer[2]}')