import re, frequencia, vocabulario, cesar

def quebrar(criptografado):

    lista_palavras = vocabulario.carregar("Lista-de-Palavras.txt")

    frases_candidatas = {}

    #Testar Rotacoes
    for rotacao in range(1, 26):
        #Rodar texto
        texto = cesar.decodificar(criptografado, rotacao)
        palavras_identificadas = []
        #Verificar presenca de cada palavra em lista
        for palavra in lista_palavras:
            #print("Palavra: " + palavra + "\n")
            if palavra in texto:
                expressao_regular = "(^| )" + palavra + "($| )"
                if re.findall(expressao_regular, texto):
                    palavras_identificadas.append(palavra)
        #Caso palavras tenham sido identificadas, submeter a analise
        if palavras_identificadas:
            frases_candidatas[rotacao] = set(palavras_identificadas)

    #Selecionar melhor frase
    maior_numero_identificadas = 0
    melhor_rot = 0
    for identidade_rot, conjunto_encontradas in frases_candidatas.items():
        quant_letras_decifradas = 0
        for palavra_decifrada in conjunto_encontradas:
            quant_letras_decifradas += len(palavra_decifrada)
        if quant_letras_decifradas > maior_numero_identificadas:
            maior_numero_identificadas = quant_letras_decifradas
            melhor_rot = identidade_rot

    #Reconstruir frase
    frase_reconstruida = criptografado.lower()
    conjunto_ideal = frases_candidatas[melhor_rot]
    for termo in conjunto_ideal:
        termo_crypto = cesar.codificar(termo, melhor_rot)
        frase_reconstruida = frase_reconstruida.replace(termo_crypto, termo)
    return frase_reconstruida


#Ler Texto criptografado
entrada = input("Digite o texto criptografado: ")
quebrado = quebrar(entrada)
print("Frase: " + quebrado)
