from random import randint

numero_computador = randint(0, 5)
print('-=-' * 20)
numero_digitado = int(input('Qual o número entre 0 e 5 que estou pensando? '))
print('-=-' * 20)

print(f'O número que você digitou é: {numero_digitado} ')
print(f'O número que estou pensando é: {numero_computador} \nPortanto, você: ')

if numero_digitado == numero_computador:
    print('ACERTOU!!!')


else:
    print('ERROU!!!')
