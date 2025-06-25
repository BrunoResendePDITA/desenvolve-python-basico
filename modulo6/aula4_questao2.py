frase = input('Digite uma frase: ')
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vogais_da_frase = [i for i in frase if i in vogais]
consoantes_da_frase = [i for i in frase if i not in vogais and i != ' ']

print('Vogais:',vogais_da_frase)
print('Consoantes:',consoantes_da_frase)

