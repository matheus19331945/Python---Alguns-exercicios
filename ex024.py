# Solicitar o nome da cidade ao usuário
cidade_usuario = input('Informe o nome de sua cidade: ')

# Converter para maiúsculas para facilitar a comparação
cidade_usuario_upper = cidade_usuario.upper()

# Verificar se a cidade começa com a palavra "SANTO"
comeca_com_santo = cidade_usuario_upper[:5] == 'SANTO'

# Exibir o resultado na tela
print(f'A cidade começa com a palavra "SANTO"? {comeca_com_santo}')
