frase = input('Digite uma frase: ')
palavra = input('Digite a palavra objetivo: ')
anagramas = []

for i in frase.split():
    if len(i) == len(palavra):
        if sorted(i.lower()) == sorted(palavra.lower()):
            anagramas.append(i)
        

print(f'Anagramas: {anagramas}')
