frase = input('Digite uma frase (digite "fim" para encerrar): ')

apenas_letras = [i.lower() for i in frase if i.isalpha()]

eh_palindromo = True

while frase != 'fim':

    for i in apenas_letras:
        for j in reversed(apenas_letras):
            if i == j:
                pass
            else:
                eh_palindromo = False

    if eh_palindromo:
        print(f'A frase: {frase} é palíndromo.')
        eh_palindromo = True
    else:
        print(f'A frase: {frase} não é palíndromo.')
        eh_palindromo = False

    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    apenas_letras = [i.lower() for i in frase if i.isalpha()]
   