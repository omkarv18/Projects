from IntegrationRules import integration_tol, simpsons
import numpy as np

def exp_func(x):
    return np.sqrt(2/(3*np.pi)) * np.exp((-2/3) * x **2 + (5/3)*x - (1/6))

answer = integration_tol(simpsons, exp_func, -17.5, 22.5, 1e-12)

print(answer)

