import random

def encrypt(lista_strings):
    chave = random.randint(1, 10)
    chave = 5
    criptografados = []

    char_alterado = ''
    string_atual = ''

    for palavra in lista_strings:
        for char in palavra:
            char_alterado = ord(char) + chave
            if char_alterado >= 127:
                char_alterado = 33 + (char_alterado - 127)
            string_atual += chr(char_alterado)

        criptografados.append(string_atual)
        string_atual = ''
    
    return criptografados

nomes = ['Luana', 'Ju', 'Davi', 'Vivi', 'Pri', 'Luiz']

resultado = encrypt(nomes)
print(f'Nomes encriptografados: {resultado}')
