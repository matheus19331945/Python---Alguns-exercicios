# Cotação do dólar para o exercício
cotacao_dolar = 5.07  # Suponha que 1 dólar = 5 reais

# Solicita ao usuário o valor que possui em reais
reais = float(input("Quantos reais você tem na carteira? R$ "))

# Calcula quantos dólares podem ser comprados
dolares = reais / cotacao_dolar

# Exibe o resultado
print(f"Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f}.")
