nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))

media = (nota1 + nota2)/2

print(f'A média entre as notas {nota1} e {nota2} é: {media:.1f}\n')

if media >= 5:
    print('Portanto o aluno está aprovado')

else:
    print('Portanto o aluno está reprovado')
