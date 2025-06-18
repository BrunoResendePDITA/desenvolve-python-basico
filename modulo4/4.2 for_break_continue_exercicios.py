# # 1

# for i in range(10, 0, -1):
#     print(i)

# # 2

# num = int(input('Digite um número: '))
# soma = 0

# for i in range(1, num+1):
#     soma += i

# print(soma)

# # 3

# media = 0

# for i in range(1, 10+1):
#     valor = int(input('Digite um valor inteiro positivo: '))
#     media += valor

# media = media / 10



# print(f'A média dos valores digitados é {media}')

# # 4

# qnt_jogos = int(input('Digite a quantidade de jogos do galo: '))
# jogo_atual = 1

# vitorias = 0
# derrotas = 0
# empates = 0
# pontuacao = 0

# for i in range(0, qnt_jogos):

#     gols_galo = int(input(f'Digite a quantidade de gols do galo no {jogo_atual}º jogo: '))
#     gols_adversario = int(input(f'Digite a quantidade de gols do adversário no {jogo_atual}º jogo: '))

#     jogo_atual += 1

#     if gols_galo > gols_adversario:
#         vitorias += 1
#         pontuacao += 3
#     elif gols_galo == gols_adversario:
#         empates += 1
#         pontuacao += 1
#     elif gols_galo < gols_adversario:
#         derrotas += 1

# print(f'Vitórias: {vitorias}')
# print(f'Empates: {empates}')
# print(f'Derrotas: {derrotas}')
# print(f'Pontuação: {pontuacao}')


# # 5

# linhas = int(input('Digite o número de linhas de um campo de batalha naval: '))
# colunas = int(input('Digite o número de colunas: '))

# indice = 0
# primeira_linha = ' '

# for i in range(1, colunas + 1):
#     primeira_linha += str(i)

# print(primeira_linha)

# for i in range(0, linhas + 1):
#     if not indice:
#         pass
#     else:
#         print(f'{indice}{"/" * colunas}')

#     indice += 1



# # 6 

# for i in range(0, 1000):
#     valor = int(input('Digite um valor: '))
#     if valor == 0:
#         break
#     else:
#         continue

        
# # 7

# produto = 0

# for i in range(0, 1000):
#     valor = int(input('Digite um valor: '))

#     if valor == 0:
#         break
#     elif valor > 0 and produto == 0:
#         produto = valor
#         continue
#     elif valor > 0 and produto > 0:
#         produto *= valor
#         continue


# print(f'Produto: {produto}')

# 8 

expressao = ''
soma = 0
operador_atual = '+'

while True:
    caractere = input('Digite um número, "+", "-" ou Fim: ')
    if caractere == 'Fim':
        break
    expressao += caractere
 
for i in expressao:
    if i == '+':
        operador_atual = '+'
        continue
    elif i == '-':
        operador_atual = '-'
    else:
        if operador_atual == '+':
            soma += int(i)
        else:
            soma -= int(i)

print(soma)

    
    


    
     



