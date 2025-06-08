def solicitar_numeros():
    while True:
        entrada = input('Informe 3 números separados por ",": ').replace(" ", "")
        numeros = entrada.split(",")

        # Verifica se a entrada contém exatamente 3 números e se todos são dígitos
        if len(numeros) == 3 and all(numero.isdigit() for numero in numeros):
            numeros = [int(numero) for numero in numeros]
            return numeros
        else:
            print('Por favor, informe exatamente 3 números válidos separados por vírgula.')

def main():
    numeros = solicitar_numeros()

    # Condição de igualdade dos 3 números
    if numeros[0] == numeros[1] == numeros[2]:
        print(f'''Todos os números são iguais, informe números diferentes!!
        Números informados: {numeros}''')
    else:
        # Definindo valor maior/menor
        numero_maior = max(numeros)
        numero_menor = min(numeros)

        print(f'O maior número é: {numero_maior} e o menor número é: {numero_menor}')

if __name__ == "__main__":
    main()
# __name__:
# É uma variável especial que o Python define para cada módulo.
# Se o módulo está sendo executado diretamente (ou seja, você está executando o arquivo como um script), __name__ é definido como "__main__".
# Se o módulo está sendo importado de outro módulo, __name__ é definido como o nome do módulo (o nome do arquivo sem a extensão .py).
#
# "__main__":
# É uma string padrão que o Python usa para identificar o script que está sendo executado diretamente.