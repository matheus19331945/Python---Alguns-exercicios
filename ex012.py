#Apresentação
print(f'{"Aplicador de descontos" :=^50}')

#usuário define os valores
preco_produto = float(input("Insira o valor atual do produto que deseja aplicar o desconto: "))
desconto_produto = float(input("Insira o valor em % que você deseja aplicar (somente números): "))

#cálculo para definir o preço final
porcentagem = preco_produto * desconto_produto / 100
preco_final = preco_produto - porcentagem

#Conclusão
print(f'Aplicado o desconto fornecido, o novo valor que temos é R${preco_final:.2f}')