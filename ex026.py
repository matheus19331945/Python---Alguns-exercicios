frase_usuario = input('Informe uma frase: ').strip()
frase_usuario = frase_usuario.upper()
print(f'''A letra "A" aparece {frase_usuario.count('A')} vezes
Primeiro na posição {frase_usuario.find('A')+1}
Segundo na posição {frase_usuario.rfind('A')+1}''')
