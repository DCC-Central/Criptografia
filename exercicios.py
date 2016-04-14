#Aula prática de python - 2
#Alunos: Henrique V. de Toledo e Lucas Rampazzo 


#Exercício 1
def resto(a, b):
    R=a
    while(R >= b):
        R = R - b

    return(R)

#Exercício 3
def mdc(a,b):
    r = 1
    while(r > 0):
        r = a % b
        a = b
        b = r

    return(a)

#Exercício 4
def parteImpar(n):

    q = n
    e = 0

    while(q % 2 == 0):
        q = q / 2
        e = e + 1


    return(e, q)


#Exercício 5

def chave(a, b, a1, b1):

    M = a*b - 1
    e = b1 * M + b
    d = a1 * M + a
    N = (e * d - 1) / M

    print("Chave publica:", N, e)
    print("Chave privada:", d)

    return(N, e, d)


def codificar(e, N, t):

    C = (e * t) % N

    return(C)

def decodificar(C, N, d):

    t = (C * d) % N

    return(t)
