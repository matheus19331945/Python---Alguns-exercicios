# Importação das bibliotecas necessárias
from datetime import date

# Solicitando informações ao usuario
ano_user = int(input("Digite o ano do nascimento: "))
ano_atual = date.today().year
print(f"Estamos no ano de: {ano_atual}")
idade_user = int(ano_atual - ano_user)

# Condições e resposta
if idade_user == 18:
    print("Está na hora de se alistar!")
elif idade_user < 18:
    print(f"Ainda não está na hora de se alistar! Faltam {18 - idade_user} anos para o alistamento! ")
elif idade_user > 18:
    print(f"Já passou da hora de se alistar! Se passou {idade_user - 18} anos para o alistamento!")