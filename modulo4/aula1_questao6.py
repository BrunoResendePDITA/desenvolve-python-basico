# 6

n = int(input('Digite a quantidade de experimentos registrados: '))
cont = 0

total = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

while cont < n:
    quantia = int(input('Digite a quantidade de cobaias utilizadas: '))
    tipo = input('Digite em maiúsculo a primeira letra do tipo de cobaia utilizada: "C", "R" ou "S": ')

    total += quantia
    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

    cont += 1

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {(total_coelhos / total) * 100:.2f}')
print(f'Percentual de ratos: {(total_ratos / total) * 100:.2f}')
print(f'Percentual de sapos: {(total_sapos / total) * 100:.2f}')
