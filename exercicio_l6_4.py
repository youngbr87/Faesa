#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 4


str(print('-----------------------------'))
str(print('      Digite um numero       '))
str(print('-----------------------------'))

soma = 0
media = 0
cont = 0

numero = int(input('Digite um número inteiro positivo => '))

while numero != -1:
    soma = soma + numero
    cont +=1
    numero = int(input('Digite um número inteiro ou [-1] para sair => '))

media = soma/cont
str(print('A média é => ', media))    