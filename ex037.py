numero_conversao = int(input('Qual o valor da conversao? '))
base_conversao = int(input('Qual será a base para a conversao? 1 - binário e 2 - octal 3 -  hexadecimal '))
if base_conversao == 1:
    print(f'O valor da conversao é {bin(numero_conversao)[2:]}')
elif base_conversao == 2:
    print(f'O valor da conversao é {oct(numero_conversao)[2:]}')
elif base_conversao == 3:
    print(f'O valor da conversao é {hex(numero_conversao)}')
else:
    print(f'Informe um valor válido para conversão')