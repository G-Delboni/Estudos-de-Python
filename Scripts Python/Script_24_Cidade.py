cidade = input('Digite o nome da sua cidade: ').title()
verificar = cidade.find('Santo')

if verificar == 0:

    print('A cidade começa com Santo')

else:

    print('A cidade não começa com Santo')