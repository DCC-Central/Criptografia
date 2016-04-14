import time
def temporesto  (a,b):
    R = a % b

    return R

comeco = time.time()
temporesto(43,8)
fim = time.time()
print(fim-comeco)
