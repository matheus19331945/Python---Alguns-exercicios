nome_usuario = input('Informe seu nome completo: ')
nome_usuario_split = nome_usuario.split()

print(f'''
Seu nome completo é {nome_usuario}
Seu primeiro nome é {nome_usuario_split[0]}
Seu último nome é {nome_usuario_split[-1]}
''')

print(f'''
\033[4:32mSeu nome completo é {nome_usuario}\033[m
\033[4:35mSeu primeiro nome é {nome_usuario_split[0]}\033[m
\033[4:39mSeu último nome é {nome_usuario_split[-1]}
''')