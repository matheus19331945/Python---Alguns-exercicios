# Solicitando dados ao usuário
nome_usuario = str(input('Informe seu nome completo: ')).strip()

# Convertendo para maiúsculas e minúsculas
nome_maiusculo = nome_usuario.upper()
nome_minusculo = nome_usuario.lower()

# Contando caracteres sem espaços
caracteres_sem_espacos = len(nome_usuario.replace(' ', ''))

# Encontrando posição do primeiro espaço
posicao_primeiro_espaco = nome_usuario.find(' ')

# Exibir dados na tela
print(f'''Nome com todas as letras maiúsculas: {nome_maiusculo}
Nome com todas as letras minúsculas: {nome_minusculo}
Sem considerar os espaços, o nome possui {caracteres_sem_espacos} caracteres
O primeiro nome possui {posicao_primeiro_espaco} letras''')