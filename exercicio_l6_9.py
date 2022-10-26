#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 9


str(print('-----------------------------'))
str(print('         Numero impar        '))
str(print('-----------------------------'))


cont =  npos = percneg = soma = num = media = quant = 0

num = int(input('Digite um número inteiro => '))

while num != 0:
    cont += 1
    soma += num
    if num > 0:
        npos += 1
    num = int(input('Digite um número inteiro => '))
print('A média é ', (soma/cont))
print('Foram digitados ', npos, 'números positivos')
print('O percentual de números negativos é ', ((cont - npos)*100)/cont, '%')
        
        





