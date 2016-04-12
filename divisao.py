def divisao(dividendo, divisor):
    quociente = 0
    resto = dividendo

    while resto >= divisor:
        resto = resto - divisor
        quociente += 1

    return quociente, resto
