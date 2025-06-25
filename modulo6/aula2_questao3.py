import random

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(random.randrange(0, 50))
    lista2.append(random.randrange(0, 50))


for i in lista1:
    for j in lista2:
        if i == j and i not in interseccao:
            interseccao.append(i)

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print(f'Interseccao: {sorted(interseccao)}')

print('Contagem')
for i in sorted(interseccao):
    print(f'{i}: (lista1={lista1.count(i)}, lista2={lista2.count(i)})')

