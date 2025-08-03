# Ler entrada do teclado
entrada = input('Digite algo: ')

# Obter tipo primitivo da entrada
tipo_primitivo = type(entrada)

# Imprimir o tipo primitivo
print(f'O tipo primitivo de "{entrada}" é: {tipo_primitivo}')

#Valida os tipos primitivos do valor
print(f'O tipo primitivo desse valor é {tipo_primitivo}')
print(f'Só tem espaços? {entrada.isspace()}')
print(f'É um número? {entrada.isnumeric()}')
print(f'É alfabético? {entrada.isalpha()}')
print(f'É alfanumérico? {entrada.isalnum()}')
print(f'Está em maiúsculas? {entrada.isupper()}')
print(f'Está em minúsculas? {entrada.islower()}')
print(f'Está capitalizado? {entrada.istitle()}')


#Valida os tipos primitivos do valor COM CORES
print(f'O tipo primitivo desse valor é \033[30m {tipo_primitivo}\033[0;0m')
print(f'Só tem espaços? \033[31m{entrada.isspace()}\033[m')
print(f'É um número? \033[32m{entrada.isnumeric()}\033[m')
print(f'É alfabético? \033[33m{entrada.isalpha()}\033[m')
print(f'É alfanumérico? \033[34m{entrada.isalnum()}\033[m')
print(f'Está em maiúsculas? \033[35m{entrada.isupper()}\033[m')
print(f'Está em minúsculas? \033[36m{entrada.islower()}\033[m')
print(f'Está capitalizado? \033[37m{entrada.istitle()}\033[m')