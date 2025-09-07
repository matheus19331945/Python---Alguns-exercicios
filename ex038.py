num1 = int(input("Informe o primeiro número inteiro: "))
num2 = int(input("Informe o segundo número inteiro: "))
if num1 > num2:
    print(f"O primeiro valor {num1} é maior que o segundo valor {num2}")
elif num2 > num1:
    print(f"O segundo valor {num2} é maior que o segundo valor {num1}")
elif num2 == num1:
    print(f"Os valores {num2} e {num1} são iguais")