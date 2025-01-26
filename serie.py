import numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 1000
def mat_mult(A, B, mod):
    return np.array([[sum(Decimal(A[i][k]) * Decimal(B[k][j]) for k in range(3)) % mod for j in range(3)] for i in range(3)], dtype=object)

def mat_pow(M, p, mod):
    result = np.eye(3, dtype=object)
    base = M
    while p > 0:
        if p % 2 == 1:
            result = mat_mult(result, base, mod)
        base = mat_mult(base, base, mod)
        p //= 2
    return result

def tribonacci(n, T1, T2, T3, mod):
    if n == 1:
        return Decimal(T1) % mod
    elif n == 2:
        return Decimal(T2) % mod
    elif n == 3:
        return Decimal(T3) % mod
    
    M = np.array([[1, 1, 1],
                  [1, 0, 0],
                  [0, 1, 0]], dtype=object)
    
    Mn = mat_pow(M, n - 3, mod)
    
    T = np.array([Decimal(T3), Decimal(T2), Decimal(T1)], dtype=object)
    
    result = sum(Mn[0, i] * T[i] for i in range(3)) % mod
    return result

TC1, TC2, TC3 = 1, 1, 1  
T1, T2, T3 = 0, 1, 2  
n = 2023202320232023  
# n = 50  # En esta posicion el resultado es 8188013234823360
mod = 10**80  # Establece la cantidad de cifras del resultado

result = tribonacci(n, TC1, TC2, TC3, mod) * 2023 + tribonacci(n, T1, T2, T3, mod)
print(result)
