#resto da divisao de dividendo por um divisor
def divisao(dividendo, divisor):

    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor
        quociente = quociente + 1
        print(resto, quociente)

    return resto, quociente

print(divisao(26,6))

print(divisao(134,5))
