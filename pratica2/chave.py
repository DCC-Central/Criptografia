def chave(a,b,a1,b1):
    M=a*b-1
    E=a1*M+a
    d=b1*M+b
    N=(E*d-1)/M
    print ("Chave Publica", N,E)
    print ("Chave Privada", d)
