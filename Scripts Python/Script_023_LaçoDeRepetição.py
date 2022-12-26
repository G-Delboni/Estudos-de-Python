while True:

    num = int(input("Digite um número de 0 a 9999: "))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 %10

    if num <= 9999:

        print(f'O número {num} é composto de:')
        print(f'Unidade: {u}')
        print(f'Dezena: {d}')
        print(f'Centena: {c}')
        print(f'Milhar: {m}')
        verificar = input('Deseja continuar? Y/N ').title()

        if verificar == "Y":

            continue

        else:

            break

    elif num > 9999:

        print('O número digitado precisa estar entre 0 e 9999')
        verificar = input('Deseja continuar? Y/N ').title()

        if verificar == "Y":

            continue

        else:

            break