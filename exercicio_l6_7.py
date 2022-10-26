#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 7

from re import A


str(print('---------------------------------'))
str(print('    Dois algoritmos A e B        '))
str(print('---------------------------------'))


soma = 0

a = int(input('Digite o valor de A => '))
b = int(input('Digite o valor de B => '))

if b > a:
    for n in range(a + 1, b):
       soma += n

    str(print('A soma entre os numeros A e B é => ', soma))

elif b < a:
    for n in range(b + 1, a):
       soma += n

    str(print('A soma entre os numeros A e B é => ', soma))
    
else:
    str(print('A e B são iguais'))        