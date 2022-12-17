salario = float(input('Digite o salário do funcionário '))
print(f'O salário do funcionário era de R${salario:.2f}')

aumento = salario * 0.15 #Ou salario * 15 / 100
salario = salario + aumento

print(f'O novo salário do funcionário será de R${salario:.2f}')