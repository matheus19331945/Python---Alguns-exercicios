# Solicitar dados ao usuário
while True:
    try:
        numero_user = int(input('Informe um número: '))
        break
    except ValueError:
        print('Por favor, digite somente números inteiros (1, 2, 3, 4, 5, ...)')
    except KeyboardInterrupt:
        print("Você interrompeu a execução do programa.")
        exit()

# Identificação do número
resto_divisao_por_2 = numero_user % 2
if resto_divisao_por_2 == 0:
    print("\033[32mO número é par\033[m")
else:
    print("\033[31mO número é ímpar\033[m")
