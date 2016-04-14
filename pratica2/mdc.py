def MDC (dividendo, divisor):
    while divisor != 0:
        dividendo2 = divisor
        divisor = dividendo % divisor
        dividendo = dividendo2
    return dividendo
