import random
import math

n = int(input('Digite a quantidade de números aleatórios a ser gerada: '))
num_atual = 0
soma = 0

for i in range(n):
    num_atual = random.randint(0, 100+1)
    print(num_atual)
    soma += num_atual

print(f'Soma: {soma}')
raiz_da_soma = math.sqrt(soma)

print(f'Raiz da soma: {raiz_da_soma}')




