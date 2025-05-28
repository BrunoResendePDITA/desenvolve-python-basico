# Pede o usuário para digitar o comprimento de um terreno e converte de string para int
comprimento = int(input("Digite o comprimento do seu terreno: "))

# Pede o usuário para digitar a largura de um terreno e converte de string para int
largura = int(input("Digite a largura do seu terreno: "))

# Pede o usuário para digitar o preço do metro quadrado de um terreno e converte de string para float
preco_m2 = float(input('Digite o preço do metro quadrado da região:'))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:.2f}")
