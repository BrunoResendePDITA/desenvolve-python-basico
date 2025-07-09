data = input('Digite sua data de nascimento (dd/mm/aaaa): ')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data_sep = data.split('/')
data_sep = [int(i) for i in data_sep]

print(f'Você nasceu em {data_sep[0]} de {meses[data_sep[1] - 1]} de {data_sep[2]}.')
