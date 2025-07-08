nome = input('Digite seu nome: ')

cont = 1
for i in range(len(nome)):
    print(nome[:cont])
    cont += 1
