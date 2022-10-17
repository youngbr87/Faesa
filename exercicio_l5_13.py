#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 13

while True:
    
    str(print('---------------------------'))
    str(print('   Divisivel por 3 ou 7    '))
    str(print('---------------------------'))

    num_1 = int(input('Informe um número (inteiro) => '))
    
    por_3 = (num_1 / 3)
    por_7 = (num_1 / 7)
    
    if (num_1 % 3) == 0:
        str(print('O numero, ', num_1, 'é divisivel por 3'))
    else:
        str(print('O numero, ', num_1, 'não divisivel por 3'))
    
    if (num_1 % 7) == 0:
           str(print('O numero, ', num_1, 'é divisivel por 7'))
    else:
        str(print('O numero, ', num_1, 'não divisivel por 7'))
        break
    
    
    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break