#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 3

from ast import Break


while True:
    print('------------------------------')
    print('     PONTUAÇÃO MAIS ALTA      ')
    print('------------------------------')
    print() 
    
    pont1 = float(input('Digite a primeira pontuaçã0 => '))
    pont2 = float(input('Digite a primeira pontuaçã0 => '))
    pont3 = float(input('Digite a primeira pontuaçã0 => '))
    
    if pont1 > pont2 > pont3:
        print('A maior pontuação foi: ', pont1)
    elif pont2 > pont1 > pont3:
        print('A maior pontuação foi: ', pont2)
    elif pont3 > pont2 > pont1:
        print('A maior pontuação foi: ', pont3) 
    print()       
    
    resp = str(input('Deseja continuar [S]/[N]'))
    if resp == 'N,n':
        break