#Solicitando valor ao usuário
valor_usuario = float(input("Informe um valor numérico: "))

#Calculando valor sucessor e antecessor
antecessor = valor_usuario - 1
sucessor = valor_usuario + 1

#Exibir dados na tela
print(f"O valor antecessor é igual a: {antecessor} e o sucessor é igual a: {sucessor}")

#Exibir dados na tela com cores
print(f"O valor antecessor é igual a: \033[4:32m{antecessor}\033[m e o sucessor é igual a: \033[4:33m{sucessor}\033[m")