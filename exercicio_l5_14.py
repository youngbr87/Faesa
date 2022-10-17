#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 14

while True:
    
    str(print('----------------------------'))
    str(print('     Linha de credito       '))
    str(print('----------------------------'))
    
    sal = float(input('Digite o salario => R$ '))
    prest = int(input('Quantas prestações => '))
    
    result = (sal / prest)
    perc = sal * 0.30
    
    if result > perc:
        str(print('Não pode ser concedido o emprestimo'))
    else:  
        str(print('Aprovado o emprestimo'))  
    
    
    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break