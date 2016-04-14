import time
def resto(a,b):
    R=a
    while R>=b:
        R=R-b
    return(R)

# resto de 43 dividido por 8
comeco = time.time()
resto(43,8)
fim = time.time()
print(fim - comeco)

