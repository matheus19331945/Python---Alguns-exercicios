# Função de aumento salarial
def aumento_salarial(valor_inicial):
    aumento_10 = 10
    aumento_15 = 15
    if valor_inicial > 1250.00:
       valor_final = valor_inicial + (valor_inicial * aumento_10 / 100)
       print(f'Valor antigo = R${valor_inicial:.2f} \nNovo valor = R${valor_final:.2f} \nAumento de {aumento_10}%')
    else:
       valor_final = valor_inicial + (valor_inicial * aumento_15 / 100)
       print(f'Valor antigo = R${valor_inicial:.2f} \nNovo valor = R${valor_final:.2f} \nAumento de {aumento_15}%')
    return valor_final

# Solicitar dados ao usuário
while True:
    try:
        salario_inicial = float(input('Informe o valor do salário: '))
        break
    except ValueError:
        print('Por favor, informe apenas números')

#Chamada de função
salario_novo = aumento_salarial(salario_inicial)

#