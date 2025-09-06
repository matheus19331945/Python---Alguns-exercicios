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

# Com cores
if numero_usuario == numero_aleatorio:
    print(f'\033[1:32mParabéns, você acertou o que eu pensei 😎\033[m')
elif numero_usuario > 5:
    print(f'\033[1:33mEu disse de 0 a 5, você é cego?\033[m')
else:
    print('\033[1;31Errooooooou\033[m')