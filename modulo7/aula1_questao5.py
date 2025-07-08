frase = input('Digite uma frase: ')

print(f'Indices {[i for i in range(len(frase)) if frase[i] in "aeiou"]}')
