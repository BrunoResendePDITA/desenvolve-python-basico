import random

numeros_aleatorios = []

for num in range(20):
    numeros_aleatorios.append(random.randint(-100, 100))

print(f'Lista ordenada: {sorted(numeros_aleatorios)}')
print(f'Lista original: {numeros_aleatorios}')
print(f'Indice do maior número: {numeros_aleatorios.index(max(numeros_aleatorios))}')
print(f'Indice do menor número: {numeros_aleatorios.index(min(numeros_aleatorios))}')
