import random

def embaralhar_palavras(frase):
    frase_modificada = []
    meio = None

    for i in frase.split():
        meio = list(i[1:-1])
        random.shuffle(meio)
        embaralhado = ''.join(meio)
        frase_modificada.append(i[0] + embaralhado + i[-1])

    frase_modificada = ' '.join(frase_modificada)

    print(frase_modificada)

frase = 'Vamos ver se funciona'

embaralhar_palavras(frase)
