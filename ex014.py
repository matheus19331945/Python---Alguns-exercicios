t = float(input('Informe a temperatura em Cº'))
print(f"{t} Cº de temperatura correspondem a {t * 1.8 + 32} Fº")

# print com cores
print(f"\033[30:44m{t} Cº de temperatura correspondem a {t * 1.8 + 32} Fº\033[m")