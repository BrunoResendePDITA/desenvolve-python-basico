frase = input('Digite uma frase: ')

for vogal in 'aeiouAEIOU':
    frase = frase.replace(vogal, '*')

print(frase)
