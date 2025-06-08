# Solicitar informações do usuário
while True:
    try:
        ano_user = int(input('Informe um ano: '))
        break
    except ValueError:
        print('Digite somente números')

# Calculo do bissexto e exibição do resultado
if (ano_user % 4 == 0 and ano_user % 100 != 0) or (ano_user % 400 == 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
