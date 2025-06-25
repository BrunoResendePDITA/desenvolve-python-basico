num_valores = int(input('Digite o número de valores da lista(4 ou mais): '))

valores = []
valor_atual = 0

for i in range(num_valores):
    valor_atual = int(input('Digite o valor atual: '))
    valores.append(valor_atual)

print('Lista original:', valores)
print('3 primeiros elementos:', valores[:3])
print('2 últimos elementos:', valores[-2:])
print('Lista invertida:', valores[::-1])
print('Elementos de índice par', valores[::2])
print('Elementos de índice ímpar', valores[1::2])
