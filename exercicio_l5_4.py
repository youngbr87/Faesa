#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 4

while True:
    str(print('====================='))
    str(print('     Número maior    '))
    str(print('====================='))
    
    num1 = int(input('Digite um número => '))
    num2 = int(input('Digite outro número => '))
    
    if num1 == num2:
        print('Os números são iguais')
    elif num1 < num2:
        print('O segundo é número é maior')
    else:
        print('O primeiro número é maior')        
        
    resp = str(input('Deseja continuar comparando? [S]/[N] => '))
    if resp in 'N,n':
        break
    