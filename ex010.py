# Cotação do dólar para o exercício
cotacao_dolar = 5.54  # Suponha que 1 dólar = 5 reais

# Solicita ao usuário o valor que possui em reais
reais = float(input("\033[32:48m Quantos reais você tem na carteira? R$ \033[m"))

# Calcula quantos dólares podem ser comprados
dolares = reais / cotacao_dolar

# Exibe o resultado
print(f"\033[32:40m Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f}\033[m.")
