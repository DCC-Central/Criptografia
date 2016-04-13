"""
Programa: Quebra Kid_RSA
Descrição: Procurar restrigir as possibilidades dos pares d e q' através
do algoritmo de Euclides estendido, ou seja, por meio da solução de uma
equação diofantina linear
Autor: Copyright 2016, Lucca Martins Felix
"""

def algoritmo_euclidiano(a, b):
	lista_resto = [a, b]
	lista_quociente = [0, 0]
	contador = 0
	while (lista_resto[-1] != 0):
		lista_quociente.append(lista_resto[contador]//lista_resto[contador+1])
		lista_resto.append(lista_resto[contador]%lista_resto[contador+1])
		
		contador += 1
	d = lista_resto[-2]
	return(d, lista_quociente)	
	
	
def cria_lista_x(lista_quociente):
	lista_x = [1, 0]
	for contador in range(2, len(lista_quociente)-1):
		lista_x.append(lista_x[contador-2]-(lista_quociente[contador]*lista_x[contador-1]))
#	print(lista_x)
	alpha = lista_x[-1]
	return(alpha)
		
def algoritmo_euclidiano_estendido(a, b, c):
	"""
	a = int(input("Diga a: "))
	b = int(input("Diga b: "))
	c = int(input("Diga c: "))
	"""
	d, lista_quociente = algoritmo_euclidiano(a, b)
	alpha = cria_lista_x(lista_quociente)
	beta = (d - (alpha*a))/b
	
	a1 = a//d
	b1 = b//d
	c1 = c//d
	
	print("A chave descoberta foi:", c1*alpha)
#	print("x =", c1*alpha, "+ k *",b1)
#	print("y =", c1*beta, "- k *",a1 )
	return(c1*alpha)
	
def gera_chave(a, b, a1, b1, t):
	m = a*b -1
	e = a1*m + a
	d = b1*m + b
	n = (e*d - 1)//m
	print("A chave gerada foi ", d)
	return(e, n, 1)

def decifrar(c, d, n):
	print("O código decifrado foi: ", c*d%n)
	
def main():
	e = int(input("Diga a chave pública e: "))
	n = int(input("Diga a chave pública N: "))
	c = int(input("Diga o número codificado: "))
	d = algoritmo_euclidiano_estendido(e, n, 1)
	decifrar(c, d, n)
	
main()

	
