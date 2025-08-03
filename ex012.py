#Apresentação
print(f'{"Aplicador de descontos" :=^50}')

#usuário define os valores
preco_produto = float(input("\033[31:40mInsira o valor atual do produto que deseja aplicar o desconto: \033[m"))
desconto_produto = float(input("\033[31:48mInsira o valor em % que você deseja aplicar (somente números): \033[m"))

#cálculo para definir o preço final
porcentagem = preco_produto * desconto_produto / 100
preco_final = preco_produto - porcentagem

#Conclusão
print(f'\033[35:48mAplicado o desconto fornecido, o novo valor que temos é R${preco_final:.2f}\033[m')