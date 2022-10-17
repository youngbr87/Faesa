#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 15

while True:
    
    str(print('-----------------------------'))
    str(print('       Emprestimo            '))
    str(print('-----------------------------'))
    
    sal_1 = float(input('Digite o valor do sálario => '))
    print()
    financ = float(input('Digite o valo do emprestimo prentendido => '))
    
    empre_5 = sal_1 * 5
    
    print()
    
    if empre_5 > financ:
        str(print('Emprestimo concedido'))
    else:
        str(print('Emprestimo negado'))
    
    print()    
        
    str(print('Obrigado por nos consultar'))    

    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break