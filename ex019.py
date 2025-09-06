#Importando bibliotecas necessárias
import random

#Solicitar dados ao usuário
nomes = input("Informe o nome dos quatro alunos inserindo uma vírgula para separar cada um: ")

# Dividir a entrada em nomes usando a vírgula como separador
nomes_divididos = nomes.split(',')

# Escolher aleatóriamente um dos nomes
nome_sorteado = random.choice(nomes_divididos)

#Exibir os dados na tela
print(f"O aluno sorteado foi o(a) {nome_sorteado} ")

#Exibir os dados na tela com cores
print(f"\033[0:34:40m O aluno sorteado foi o(a) {nome_sorteado} \033[m")