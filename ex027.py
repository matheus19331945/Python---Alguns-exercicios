nome_usuario = input('Informe seu nome completo: ')
nome_usuario_split = nome_usuario.split()

print(f'''
Seu nome completo é {nome_usuario}
Seu primeiro nome é {nome_usuario_split[0]}
Seu último nome é {nome_usuario_split[-1]}
''')