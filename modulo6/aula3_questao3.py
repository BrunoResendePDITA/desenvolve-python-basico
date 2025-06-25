import random

lista = []

for i in range(20):
    lista.append(random.randint(-10, 10))


maior_invervalo_atual = 0
maior_invervalo_anterior = 0
maior_intervalo_final = 0

for i in lista:
    if i < 0:
        maior_invervalo_atual += 1

    if i >= 0:
        if maior_intervalo_final < maior_invervalo_atual:
            maior_intervalo_final = maior_invervalo_atual

        maior_invervalo_anterior = maior_invervalo_atual
        maior_invervalo_atual = 0

maior_invervalo_atual = 0
maior_invervalo_anterior = 0

print(lista)

cont = 0
for i in lista:
    if i < 0:
        maior_invervalo_atual += 1

    if i >= 0 and maior_invervalo_atual == maior_intervalo_final:
        del lista[cont-maior_intervalo_final : cont]
        break

    if i >= 0:
        maior_invervalo_atual = 0

    cont += 1

print(lista)
