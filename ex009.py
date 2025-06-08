# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro para ver sua tabuada: "))

# Exibe a tabuada do número inserido
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")