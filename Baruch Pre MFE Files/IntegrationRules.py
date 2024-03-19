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
    return np.array(final_values)

def r_t(t):
    return 0.05 / (1 + np.exp(-(1 + t) ** 2))

def N_t(t):
    return np.exp(-t **2 / 2)

np.set_printoptions(precision=14)

# answer = np.exp(-1 * integration_tol(simpsons, r_t, 0, 3, 1e-6))

answer2 = 0.5 + (1 / np.sqrt(2*np.pi)) * integration_tol(simpsons, N_t, 0, 1.0, 1e-12)

# print('hi', answer2)