#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 6

str(print('-----------------------------'))
str(print('     Concurso de beleza      '))
str(print('-----------------------------'))

maior =  0
alt = float(input('Digite a altura da moça ou zero para sair => '))

while alt != 0:
    if alt > maior:
        maior = alt  
    alt = float(input('Digite a altura da moça ou zero para sair => '))    
                 
str(print('A moça mais alta tem: ', maior)) 