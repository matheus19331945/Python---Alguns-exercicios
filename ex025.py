# Solicitar o nome do usuário
nome_usuario = input('Informe o seu nome completo: ')

# Converter para maiúsculas para facilitar a comparação
nome_usuario_upper = nome_usuario.upper()

# Verificar se o nome possui a palavra "SILVA"
possui_silva = 'SILVA' in nome_usuario_upper

# Exibir o resultado na tela
print(f'O nome possui a palavra "SILVA"? {possui_silva}')
