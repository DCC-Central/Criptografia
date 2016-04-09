#Programa: vocabulario.py
#Descrição: Retorna o vocabulário de um dado texto.

import re

def carregar(fonte):
    arquivo = open(fonte)
    corpo_literario = open(fonte, "r", errors='ignore').read().lower()

    regex = "[a-z]+(?:(?:'|-)[a-z]+)?(?:(?:'|-)[a-z]+)?"
    palavras = re.findall(regex, corpo_literario)
    palavras_unicas = set(palavras)

    return palavras_unicas
