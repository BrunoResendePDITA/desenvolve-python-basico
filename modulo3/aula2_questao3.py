idade = int(input("Digite sua idade: "))

jogou_3_jogos = bool(int(input("Digite '1' se já jogou 3 jogos, do contrário digite '0': ")))

vezes_venceu = bool(input("Digite quantos jogos já venceu: "))

print("Apto para ingressar no clube: ", (idade > 15 and idade < 19) and jogou_3_jogos and (vezes_venceu > 0))