#para usar no terminal, use python3.5 RSAkid_test.py


print("Defina seu cartão de crédito, a, b, a', b'")
t = int(input("max 2 dígitos "))
a = int(input("a:"))
b = int(input("b:"))
a1 = int(input("a':"))
b1 = int(input("b':"))

m = a * b - 1
e = a1 * m + a
d = b1 * m + b
n = ((e*d) - 1) / m
#codificação
C = (e*t) % n
print("O bandido verá esse código:\n" , str(C))
#decodificação
D = (C*d) % n
print("A Amazon verá\n", str(D))
