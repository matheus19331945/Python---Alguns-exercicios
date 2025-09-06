#Importando bibliotecas necessárias
import random

#Solicitar dados ao usuário
nomes = input("Informe o nome dos quatro alunos inserindo uma vírgula para separar cada um: ")

# Dividir a entrada em nomes usando a vírgula como separador
nomes_divididos = nomes.split(',')

# Embaralhando a ordem dos alunos para apresentação de trabalho
#O Shuffle é o que chamam de "in-place" ele altera diretamente a variável, então não precisa atribuir a outra
# Quando você faz nome_sorteado = random.shuffle(nomes_divididos), está atribuindo o valor de retorno da função shuffle() à variável nome_sorteado, e esse valor é None
random.shuffle(nomes_divididos)

#Exibir dados na tela
print(f"A ordem de apresentação é: {nomes_divididos}")

#Exibir dados na tela com cores
print(f"\033[0:36:47m A ordem de apresentação é: {nomes_divididos}\033[m")
