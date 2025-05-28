# Programa que converte Fahrenheit em graus Celsius

temp = int(input('Digite uma temperatura em graus Fahrenheit: '))

conversao_em_celsius = (temp - 32) * (5/9)
conversao_em_celsius = int(conversao_em_celsius)

print(f'{temp} graus Fahrenheit são {conversao_em_celsius} graus Celsius.')
