#Importando bibliotecas necessárias
import random
from emoji import emojize

#Solicitando dados ao usuário
numero_usuario = int(input('Digite um número de 0 a 5: '))

#Selecionando número aleatoriamente
numero_aleatorio = random.randint(0,5)

#Condição de acerto/erro
if numero_usuario == numero_aleatorio:
    print(f'Parabéns, você acertou o que eu pensei 😎')
elif numero_usuario > 5:
    print(f'Eu disse de 0 a 5, você é cego?')
else:
    print('Errooooooou')