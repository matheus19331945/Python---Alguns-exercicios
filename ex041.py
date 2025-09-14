# Importação das bibliotecas necessárias
from datetime import date

ano_atual = date.today().year
ano_nascimento_atleta = int(input('Informe o ano de nascimento do atleta: '))
idade_atleta = ano_atual - ano_nascimento_atleta
if idade_atleta <= 9:
    print('A categoria do atleta é: MIRIM')
elif idade_atleta <= 14:
    print('A categoria do atleta é: INFANTIL')
elif idade_atleta <= 19:
    print('A categoria do atleta é: JUNIOR')
elif idade_atleta <= 20:
    print('A categoria do atleta é: SENIOR')
else:
    print('A categoria do atleta é MASTER')
