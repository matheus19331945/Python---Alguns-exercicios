
#Importando biblioteca necessária e solicitando dados ao usuário
import math
numero_real = float(input("Informe um número real (Ex. 6.127): "))
numero_inteiro = math.trunc(numero_real)

#Se eu utilizar o "math.trunc" ele irá transformar o numero para o numero inteiro mais próximo do 0

#Exibir dados na tela
print(f"A porção inteira de {numero_real} é {numero_inteiro}")
