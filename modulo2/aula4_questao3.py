produto_1 = input('Digite o nome do produto 1: ')
preco_unitario_1 = float(input('Digite o preço unitário do produto 1: '))
quantidade_1 = int(input('Digite a quantidade do produto 1: '))

produto_2 = input('Digite o nome do produto 2: ')
preco_unitario_2 = float(input('Digite o preço unitário do produto 1: '))
quantidade_2 = int(input('Digite a quantidade do produto 2: '))

produto_3 = input('Digite o nome do produto 3: ')
preco_unitario_3 = float(input('Digite o preço unitário do produto 1: '))
quantidade_3 = int(input('Digite a quantidade do produto 3: '))

print(f'Total: R${(preco_unitario_1 * quantidade_1 + preco_unitario_2 * quantidade_2 + preco_unitario_3 * quantidade_3):,.2f}')
