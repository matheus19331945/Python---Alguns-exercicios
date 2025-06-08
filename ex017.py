#Importando bibliotecas necessárias
import math

#Solicitar dados ao usuário
cateto_oposto = float(input("Informe o valor do comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o valor do comprimento do cateto adjacente: "))

#Realizando os cálculos
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

#Exibindo valor na tela
print(f"O comprimento da hipotenusa é:  {hipotenusa:.2f}")