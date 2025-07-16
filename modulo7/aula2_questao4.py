def validador_senha(senha):
    
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_char_esp = False
    
    for char in senha:
        if char.isupper() and not tem_maiuscula:
            tem_maiuscula = True
        if char.islower() and not tem_minuscula:
            tem_minuscula = True
        if char.isdigit() and not tem_digito:
            tem_digito = True
        if not char.isalnum() and not tem_char_esp:
            tem_char_esp = True
        
    if not(tem_maiuscula and tem_minuscula and tem_digito and tem_char_esp):
        return False
    
    return True

senha1 = 'Senha123@'
senha2 = 'senhafraca'
senha3 = 'Senha_fraca'

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))