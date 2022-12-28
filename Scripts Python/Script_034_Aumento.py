salario = float(input('Digite o salário: '))

if salario > 1250:
    aumento = salario * 0.10
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} receberá um aumento de R${aumento:.2f} e passará a ser R${salario_novo:.2f}')

else:
    aumento = salario * 0.15
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} receberá um aumento de R${aumento:.2f} e passará a ser R${salario_novo:.2f}')