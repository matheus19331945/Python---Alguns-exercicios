#Apresentação
print(f'{"Promoção salarial" :=^50}')

#Solicitando dados ao usuário
salario_atual = float(input("Insira o valor do salário atual (utilize o ponto para separar os centavos): "))
percent_aumento = float(input("Insira o valor em % de aumento do salário do funcionário (apenas números): "))

#Calculo do aumento
porcentagem = salario_atual * percent_aumento / 100
salario_final = salario_atual + porcentagem

#Conclusao
print(f'Salario atualizado com sucesso, o novo valor é R${salario_final :.2f}')

#Exibindo versão alternativa
print(f'Salário definido com sucesso, o novo valor é R${salario_atual * percent_aumento / 100 + salario_atual  :.2f}')

#Exibindo versão com cores
print(f'\033[35;40m Salario atualizado com sucesso, o novo valor é R${salario_final :.2f}\033[m')