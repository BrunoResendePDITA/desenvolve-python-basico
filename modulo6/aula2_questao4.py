lista1 = []
lista2 = []
lista_intercalada = []

qnt_elem_lista1 = int(input('Digite a quantidade de elementos da lista 1: '))

print('Digite os elementos da lista 1: ')
for i in range(qnt_elem_lista1):
    num_atual = int(input(''))
    lista1.append(num_atual)

qnt_elem_lista2 = int(input('Digite a quantidade de elementos da lista 2: '))

print('Digite os elementos da lista 2: ')
for i in range(qnt_elem_lista2):
    num_atual = int(input(''))
    lista2.append(num_atual)

cont1 = 0
cont2 = 0

while cont1 + cont2 < len(lista1) + len(lista2):
    if cont1 < len(lista1):
        lista_intercalada.append(lista1[cont1])
        cont1 += 1
    if cont2 < len(lista2):
        lista_intercalada.append(lista2[cont2])
        cont2 += 1

print(lista_intercalada)
