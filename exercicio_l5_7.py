#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 7

while True:
    
    str(print('-----------------------------'))
    str(print(' Diferença entre 2 numeros   '))
    str(print('-----------------------------'))
    
    num1 = float(input('Digite um número => '))
    num2 = float(input('Digite outro número => '))
    
    dif = (num1 - num2)
    
    str(print('A diferença entre os dois números é ', dif))
    
    resp = str(input('Deseja continuar ? [S]/[N] =>'))
    if resp in 'N,n':
        break
