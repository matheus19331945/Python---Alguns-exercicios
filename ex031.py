# Solicitar dados ao usuário
while True:
    try:
        viagem_user = float(input('Informe a distância de uma viagem: '))
        if viagem_user <= 0:
            print('0 km não é considerado uma viagem.')
        else:
            break
    except ValueError:
        print('Insira somente números.')

# Definir os preços das passagens
preco_viagem_curta = 0.50
preco_viagem_longa = 0.45

# Função para calcular o preço da passagem
def calcular_preco(viagem_user, preco_curto, preco_longo):
    if viagem_user <= 200:
         return viagem_user * preco_curto
    else:
         return viagem_user * preco_longo

# Calcular e exibir o preço da passagem
preco_passagem = calcular_preco(viagem_user, preco_viagem_curta, preco_viagem_longa)
print(f'O preço da sua viagem será de R${preco_passagem:.2f}')