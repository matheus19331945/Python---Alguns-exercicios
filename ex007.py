# Solicitando ao usuário as notas
nota_aluno1 = float(input("Insira a nota do primeiro aluno, utilizando ponto para valores decimais: "))
nota_aluno2 = float(input("Insira a nota do segundo aluno, utilizando ponto para valores decimais: "))

# Calculando a média
media_2alunos = (nota_aluno1 + nota_aluno2) / 2

# Exibindo os dados
print(f"A média entre {nota_aluno1:.1f} e {nota_aluno2:.1f} é igual a {media_2alunos:.1f}")