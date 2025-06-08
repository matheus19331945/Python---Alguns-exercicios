#Importação das bibliotecas necessárias
import math

#Solicita dados ao usuáio
angulo = float(input("Informe um ângulo qualquer: "))

#Realizando cálculo do Seno, Cosseno e Tangente deste angulo
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#Exibir dados na tela
print(f"Sobre o ângulo informado de {angulo}. Segue abaixo os valores:\n seno: {seno:.2f}\n cosseno: {cosseno:.2f}\n tangente: {tangente:.2f}")