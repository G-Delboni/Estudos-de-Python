num = int(input('Digite um número inteiro de 0 a 9999: '))

unidade = (float(str(num/1000)[4:]))

if unidade >= 1:

    print(f'Unidade: {unidade}')

else:
    print('')