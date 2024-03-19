import numpy as np

def bond_price(r_zero, n, t_cash_flow, v_cash_flow):

    # n = number of cashflows
    # t_cash_flow = vector of cash flow dates (of size n)
    # v_cash_flow = vector of cash flows (of size n)
    # r_zero(t) = zero rate function corresponding to time t

    B = 0
    disc = np.empty(n)

    for i in range(n):
        disc[i] = np.exp(-t_cash_flow[i] * r_zero(t_cash_flow[i]))
        B += v_cash_flow[i] * disc[i]

    return B


def zero_rate_curve(t):
    return 0.05 + 0.005 * np.sqrt(1+t)

def zero_rate_curve2(t):
    return 0.02 + (t / (200 - t))


face_value = 100
coupon_rate = 0.04
T = 19
months = 3
n = int(np.ceil(T / months)) # (T / months) & round up
t_cash_flow = [(T / 12.0) - ((months / 12.0) * j) for j in range(n)]
t_cash_flow = np.array(t_cash_flow[::-1].copy())
v_cash_flow = [(coupon_rate / (12 / months)) * face_value for _ in range(n-1)]
v_cash_flow.append((coupon_rate / (12 / months)) * face_value + face_value)

v_cash_flow = np.array(v_cash_flow.copy())

print(n)
print(t_cash_flow)
print(v_cash_flow)

answer = bond_price(zero_rate_curve2, n, t_cash_flow, v_cash_flow)

print(answer)