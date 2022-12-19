num = int(input('Digite um número de 0 a 9999: '))
n2 = str(int(10000 + num)) # A variável num é incorporada à variável n2, portanto se for menor que o número total de dígitos o código não quebra, já que o print vai exibir o valor "0" para as casas que estão faltando.


print(f'Unidade: {n2[4]}\nDezena: {n2[3]}\nCentena: {n2[2]}\nMilhar: {n2[1]}')