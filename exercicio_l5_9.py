#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 9

while True:
    
    str(print('----------------------------'))
    str(print('     Idadade do nadador     '))
    str(print('----------------------------'))
    
    age = int(input('Digite a idade do atleta => '))
    
    if (age > 5) and (age < 7):
        str(print('O atleta é INFANTIL A')) 
    
    elif (age > 8) and (age < 11):
        str(print('O atleta é INFANTIL B'))
    
    elif (age > 12) and (age < 13):
        str(print('O atleta é JUVENIL A'))        
    
    elif (age > 14) and (age <= 17):
        str(print('O atleta é JUVENIL B'))
        
    elif age > 18:
        str(print('O atleta é ADULTO'))
    
    else:
        str(print('Não classificado'))        
    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
         break 
