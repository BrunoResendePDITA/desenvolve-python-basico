# 5

n = int(input('Digite o número de respondentes da pesquisa: '))
cont = 0
soma_idades = 0

while cont < n:
    idade = int(input('Digite a idade do respondente: '))
    soma_idades += idade
    cont += 1

media_idades = soma_idades/n

print(f'A média de idade dos respondentes da pesquisa é: {media_idades}')
