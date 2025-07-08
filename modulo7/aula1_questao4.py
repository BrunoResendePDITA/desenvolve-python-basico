num = input('Digite um número de celular: ')
if len(num) == 9:
    if num[0] == '9':
        print(f'Número completo: {num[0:5] + "-" + num[5:]}')
    else:
        print('Número não começa com "9".')

elif len(num) == 8:
    print(f'Número completo: {"9" + num[0:4] + "-" + num[4:]}')


