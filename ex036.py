print('========== EMPRÉSTIMO BANCÁRIO ===============')

# Entradas do usuário
valor_casa = float(input('Digite o valor da casa: R$ '))
salario_comprador = float(input('Digite o salário do comprador: R$ '))
anos_pagamento = int(input('Digite em quantos anos pretende pagar: '))

# Cálculo de dados importantes
limite_prestacao = salario_comprador * 0.3  # 30% do salário, ou seja, o calculo aqui é o mesmo que x 30 /100, a intenção é encontrar o valor limite que o pagador poderá fazer por mês
total_meses = anos_pagamento * 12  # Total de meses
prestacao_mensal = valor_casa / total_meses  # Valor da prestação mensal real

# Decisão do empréstimo
if prestacao_mensal <= limite_prestacao:
    print(f'Empréstimo APROVADO! A prestação mensal será de R$ {prestacao_mensal:.2f}')
else:
    print(f'Empréstimo NEGADO! A prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do salário.')
