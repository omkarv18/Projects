import numpy as np


def simpsons(func, a, b, n):
    # a = left endpoint
    # b = right endpoint
    # n = number of patition intervals
    # func = routine evaluating f(x)

    h = (b - a) / n
    I_simpson = (func(a) / 6) + (func(b) / 6)

    for i in range(1, n):
        I_simpson += func(a + i * h) / 3
    
    for i in range(1, n+1):
        I_simpson += 2 * func(a + ((i - 0.5) * h)) / 3

    I_simpson *= h

    return I_simpson


def integration_tol(integration_rule, func, a, b, tol):

    n = 4
    I_old = integration_rule(func, a, b, n)

    n *= 2
    I_new = integration_rule(func, a, b, n)

    final_values = []
    final_values.append(I_old)
    final_values.append(I_new)


    while np.abs(I_new - I_old) > tol:
        
        I_old = I_new
        
        n *= 2
        
        I_new = integration_rule(func, a, b, n)
        # print(I_new)
        final_values.append(I_new)
        

    # print(n)
    I_approx = I_new
    
    # print(I_approx)
    # return np.array(final_values)
    return I_approx



def bond_price_inst(r_inst, n, t_cash_flow, v_cash_flow, tol):

    # n = number of cashflows
    # t_cash_flow = vector of cash flow dates (of size n)
    # v_cash_flow = vector of cash flows (of size n)
    # r_inst(t) = instantaneous interest rate function corresponding to time t
    # tol = vector of tolerances (of size n)

    B = 0

    I_numerical = np.empty(n)
    disc = np.empty(n)

    for i in range(n):
        I_numerical[i] = integration_tol(simpsons, r_inst, 0, t_cash_flow[i], tol[i])
        disc[i] = np.exp(-I_numerical[i])
        B += v_cash_flow[i] * disc[i]

    return disc, B


def inst_curve(t):
    return 0.05 / (1 + 2 * np.exp(-(1 + t) ** 2))

def inst_curve2(t):
    return 0.0525 + (1 / (100 * (1 + np.exp(-t ** 2))))


face_value = 100
coupon_rate = 0.05
T = 24
months = 6
tol = np.array([1e-6, 1e-6, 1e-6, 1e-8])

n = int(np.ceil(T / months)) # (T / months) & round up
t_cash_flow = [(T / 12.0) - ((months / 12.0) * j) for j in range(n)]
t_cash_flow = np.array(t_cash_flow[::-1].copy())
v_cash_flow = [(coupon_rate / (12 / months)) * face_value for _ in range(n-1)]
v_cash_flow.append((coupon_rate / (12 / months)) * face_value + face_value)

v_cash_flow = np.array(v_cash_flow.copy())

print(n)
print(t_cash_flow)
print(v_cash_flow)

np.set_printoptions(precision=14)

answer = bond_price_inst(inst_curve, n, t_cash_flow, v_cash_flow, tol)

print(answer)
