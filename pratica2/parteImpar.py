def parteImpar (n):
    E=0
    Q=n
    while Q%2==0:
        Q=Q/2
        E=E+1
    return E,Q



