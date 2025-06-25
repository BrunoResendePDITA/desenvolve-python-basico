pares_entre_20_e_50 = [i for i in range(20,51,2)]
print(pares_entre_20_e_50)

quadrados_1_a_7 = [i**2 for i in range(7+1)]
print(quadrados_1_a_7)

divisiveis_por_7 = [i for i in range(1,100+1) if i % 7 == 0]
print(divisiveis_por_7)

par_ou_impar = ['par' if i % 2 == 0 else 'impar' for i in range(0,30,3)]
print(par_ou_impar)
