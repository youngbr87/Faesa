#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 1

from ast import While


while True:
    print('------------------------------')
    print('     EXERCICIO IDADE          ')
    print('------------------------------')
    print()
    idade = int(input('Digite uma idade => '))
    if (idade >= 10) and (idade <= 18):
        print('A idade está entre 10 a 18 anos')
    else:
        print('A idade não está entre 10 a 18 anos.')
    
    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break
 