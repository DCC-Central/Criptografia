def codificar(texto, rot):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    codificado = ""

    for letra in texto.lower():
        if letra in alfabeto:
            posicao = alfabeto.index(letra) + rot
            if posicao >= 26:
                posicao -= 26
            codificado += alfabeto[posicao]
        else:
            codificado += letra

    return codificado

def decodificar(texto, rot):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    decodificado = ""

    for letra in texto.lower():
        if letra in alfabeto:
            posicao = alfabeto.index(letra) - rot
            if posicao >= 26:
                posicao -= 26
            decodificado += alfabeto[posicao]
        else:
            decodificado += letra

    return decodificado
