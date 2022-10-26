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
alt = 1

while alt != 0:
    alt = float(input('Digite a altura da moça ou zero para sair => '))
    if alt > maior:
        maior = alt  
        
                 
str(print('A moça mais alta tem: ', maior)) 