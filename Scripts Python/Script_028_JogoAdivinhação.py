from random import randint

numero_computador = randint(0, 5)
numero_digitado = int(input('Qual o número que estou pensando? '))

print(f'O número que você digitou é: {numero_digitado} ')
print(f'O número que estou pensando é: {numero_computador} \nPortanto, você: ')

if numero_digitado == numero_computador:
    print('ACERTOU!!!')


else:
    print('ERROU!!!')
