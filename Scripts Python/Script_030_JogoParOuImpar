from random import randint

num_jogador = int(input('Digite um número: '))
lado = input('Você quer ser par ou impar?: ').upper() .strip()
num_pc = randint(0, 10)
verify = (num_jogador + num_pc) % 2

if lado == "PAR":
    if verify == 0:
        print(f'Você escolheu o número {num_jogador} e eu escolhi o número {num_pc}, o resultado foi {num_pc + num_jogador}. Portanto você GANHOU!!')

    else:
        print(f'Você escolheu o número {num_jogador} e eu escolhi o número {num_pc}, o resultado foi {num_pc + num_jogador}. Portanto você PERDEU!!')

else:
    if verify == 0:
        print(f'Você escolheu o número {num_jogador} e eu escolhi o número {num_pc}, o resultado foi {num_pc + num_jogador}. Portanto você PERDEU!!')

    else:
        print(f'Você escolheu o número {num_jogador} e eu escolhi o número {num_pc}, o resultado foi {num_pc + num_jogador}. Portanto você GANHOU!!')
