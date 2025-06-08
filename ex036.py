#Valor da casa, saláro do comprador , anos para pagar
#Clcular o valor da prestação mensal, nao pode exceder 30% do salario ou o emprestimo será negado
#Entrada =
#Saida

# Introduction
print('==========BANK=LOAN===============')
house_value = float(input('Enter the house value: '))
    # Calculate 30% of the salary
buyer_wage = float(input('Enter the wage of the buyer: '))
monthly_payment = buyer_wage * 30 / 100
    # Calculate the numbers of months
years_to_pay = int(input('Enter the number of years to pay: '))
months_to_pay = years_to_pay * 12

# Total value the buyer can afford
total_affordable = monthly_payment * months_to_pay

if total_affordable >= house_value:
    print(f'Loan approved! Congratulations! The monthly payment will be R$ {buyer_wage:.2f}')
elif total_affordable < house_value:
    print('Loan denied. Reason: The monthly payments exceeds 30% of the salary.')
else:
    print('Internal server error, please contact the administrator')

