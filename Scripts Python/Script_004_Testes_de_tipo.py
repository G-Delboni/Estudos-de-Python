v = input('Digite algo ')
print (type(v) , f' \n O caractere digitado é maiúsculo? {v.isupper()}' , f' \n O caractere digitado é minúsculo? {v.islower()}'
, f' \n O caractere digitado é numérico? {v.isnumeric()}', f' \n O caractere digitado é uma letra do alfabeto? {v.isalpha()}' 
, f' \n O caractere digitado é alphanumérico? {v.isalnum()}' , f' \n O caractere digitado é um número decimal? {v.isdecimal()}')
