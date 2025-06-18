import random

num = random.randint(1, 10)
palpite = 0

while palpite != num:
    palpite = int(input('Advinhe o número entre 1 e 10: '))
    if palpite > num:
        print('Muito alto, tente novamente!')
    elif palpite < num:
        print('Muito baixo, tente novamente!')
    else:
        print(f'Correto! O número é {num}.')
