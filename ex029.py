#Solicitando dados ao usuário
while True:
    try:
        velocidade_carro = float(input('Informe a velocidade do carro APENAS NÚMEROS: '))
        break
    except ValueError:
        print("Por favor, insira apenas números.")

#Aplicando condição de multa
limite_velocidade = 80.0
if velocidade_carro > limite_velocidade:
    multa = (velocidade_carro - limite_velocidade) * 7.00
    print(f'''O motorista foi multado por exceder o limite de velocidade de {limite_velocidade} km/h
     em {velocidade_carro - limite_velocidade:.2f} km/h. Valor da multa: R$ {multa:.2f}''')
else:
    print('Velocidade dentro do limite.')
    print('\033[32mVelocidade dentro do limite.\033[m') # Com cores

