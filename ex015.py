#Apresentação
print(f'{"Aluguel de carros" :=^50}')

#Solicitando os dados ao usuário
km_percorrido = float(input("Quantos km percorrido pelo carro? "))
qtde_dias = int(input("Quantos dias que o carro foi alugado? "))

#Sabendo que o carro custa 60,00$ por dia e 0,15$ por km rodado
#Realizando o cálculo
valor_pagamento = float((km_percorrido * 0.15) + (qtde_dias * 60))

#Exibir dados na tela
print(f"O valor a se pagar pelo aluguel do carro é igual a: R$ {valor_pagamento:.2f}")

#Exibir dados na tela com cores
print(f"\033[37:40mO valor a se pagar pelo aluguel do carro é igual a: R$ {valor_pagamento:.2f}\033[m")
