#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 8

while True:

    str(print('----------------------'))
    str(print('       Salário        '))
    str(print('----------------------'))
    
    print()


    sal = float(input('Qual o salário atual => '))

    sal1 = sal * 0.15
    sal2 = sal * 0.10
    sal3 = sal * 0.05

    if sal < 500:
        print('O  reajuste de salário vai ser: ', sal1)

    elif (sal >= 500) and (sal <= 1000):
        print('O  reajuste de salário vai ser: ', sal2)    
    else: 
        print('O  reajuste de salário vai ser: ', sal3)
    
    print()    
                
    resp = str(input('Deseja continhar ? [S]/[N] => '))
    if resp in 'N,n':
        break    
  