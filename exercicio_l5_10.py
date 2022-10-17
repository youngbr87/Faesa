#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 10

while True:
    
    str(print('--------------------------------'))
    str(print('     Horario aula / Salario     '))
    str(print('--------------------------------'))
    
    
    hora_aula = float(input('Digite o valor da hora aula => R$ '))
    aulas_dadas = int(input('Digite o numero de aulas por mês => '))
    desc_inss = float(input('Digite o percentual do INSS => '))
    
    sal_bruto = hora_aula * aulas_dadas
    sal_liqui = sal_bruto - (sal_bruto *(desc_inss/100))
    
    print(('Salario liquido => '), sal_liqui)
    print(('Salario bruto => '), sal_bruto)
    
    if (sal_liqui / 1200 ) > 10:
        str(print('Sortudo'))
    elif (sal_liqui / 1200 ) > 5:
        str(print('Sortudo'))
    else:
        str(print('Ah coitado'))
         
    
   
        
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
       break