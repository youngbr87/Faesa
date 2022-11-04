str(print('-----------------------------'))
str(print('      MATERIAL DE CONSTRUÇÀO '))
str(print('-----------------------------'))


a_compra = int(input('Quantos sacos de areia o cliente vai levar => '))
b_compra = int(input('Quantos sacos de brita o cliente vai levar => '))

total_a = a_compra * 15
total_b = b_compra * 20
total_g = total_a + total_b

str(print('O valor total é: ', total_g))

if total_g > 1000:
    total_g = total_g - (total_g * 0.10)
    str(print('A compra teve desconto  => ', total_g))
else:
    str(print('A compra não teve desconto'))   
