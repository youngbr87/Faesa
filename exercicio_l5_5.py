#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 5

while True:
    
    str(print('------------------------------------'))
    str(print('   Positivo, negativo ou nulo       '))
    str(print('------------------------------------'))
    
    num1 = float(input('Digite um número => '))
    
    if num1 == 0:
        str(print('O algorismo é nulo.'))
    elif num1 > 0:
        str(print('O algorismo é positivo.'))
    else:
        str(print('O algorismo é negativo.'))
        
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break    
            