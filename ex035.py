# Solicitar valor ao usuário
reta1 = int(input('Informe o comprimento da reta 1: '))
reta2 = int(input('Informe o comprimento da reta 2: '))
reta3 = int(input('Informe o comprimento da reta 3: '))

# Verificar se os três lados podem formar um triângulo
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Os lados informados podem formar um triângulo.')
else:
    print('Os lados informados não podem formar um triângulo.')
