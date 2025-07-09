cpf = input('Digite um cpf na forma XXX.XXX.XXX-XX: ')
soma1 = 0
soma2 = 0
digito1 = None
digito2 = None
multiplicador1 = 10
multiplicador2 = 11

for num in cpf[0:3] + cpf[4:7] + cpf[8:11]:
    soma1 += int(num) * multiplicador1
    multiplicador1 -= 1

if soma1 % 11 < 2:
    digito1 = 0
else:
    digito1 = 11 - soma1 % 11

for num in cpf[0:3] + cpf[4:7] + cpf[8:11] + str(digito1):
    soma2 += int(num) * multiplicador2
    multiplicador2 -= 1

if soma2 % 11 < 2:
    digito2 = 0
else:
    digito2 = 11 - soma2 % 11

cpf_validado = cpf[0:12] + str(digito1) + str(digito2)

if cpf == cpf_validado:
    print('O CPF digitado é válido.')
else:
    print('O CPF digitado não é valido.')
