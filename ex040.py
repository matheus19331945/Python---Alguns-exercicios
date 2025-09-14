nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('\033[4;31mReprovado!\033[m')
elif media >= 5 and media < 6.9:
    print('\033[4;32mAprovado!\033[m')
elif media >= 6.9:
    print('\033[4;33mAprovado!\033[m')
