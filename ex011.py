# Solicita ao usuário a largura e a altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária
# Cada litro de tinta cobre uma área de 2 metros quadrados
quantidade_tinta = area / 2

# Exibe os resultados
print(f"A área da parede é de {area:.2f} metros quadrados.")
print(f"Você precisará de {quantidade_tinta:.2f} litros de tinta para pintar a parede.")
