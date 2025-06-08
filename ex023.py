# Solicitar um número ao usuário e validar se está no intervalo desejado
numero_usuario = int(input('Informe um número de 0 a 9999: '))
if numero_usuario < 0 or numero_usuario > 9999:
    print("Número fora do intervalo desejado. Por favor, informe um número de 0 a 9999.")
    exit('400 error')

# Separar os dígitos em unidades, dezenas, centenas e milhares
unidade = numero_usuario % 10
dezena = (numero_usuario // 10) % 10
centena = (numero_usuario // 100) % 10
milhar = (numero_usuario // 1000) % 10

# Exibir os dígitos separados na tela
print(f'''Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}''')