#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 2

while True:
    print('------------------------------')
    print('     O NUMERO É IGUAL         ')
    print('------------------------------')
    print() 
    
    num = float(input('Digite um número =>' ))
    if num == 1.5:
        print('O número é igual 1,5')
    elif num == 10:
        print('O número é igual a 10')
    else:
        print('O número digitado nao é 1,5 nem 10')        
        
            
    
    
    
        resp = str(input('Deseja continuar [S]/[N] => ')).upper()
        if resp == 'N':
            break
