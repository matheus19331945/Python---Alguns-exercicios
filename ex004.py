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