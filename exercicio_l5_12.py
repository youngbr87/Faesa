#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 12

while True:
    
    str(print('------------------------'))
    str(print('      Triangulo         '))
    str(print('------------------------'))
    
    lado1 = int(input('Digite o valor do lado 1 => '))
    print()
    lado2 = int(input('Digite o valor do lado 2 => '))
    print()
    lado3 = int(input('Digite o valor do lado 3 => '))
    
    print()
    
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        str(print('Não é um triangulo'))
    
    elif lado1 > (lado2 + lado3) or lado2 > (lado1 + lado2) or lado3 > (lado1 + lado2):
        str(print('Não é um triangulo'))
        
    elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        str(print('É um triangulo equilatreo'))
       
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        str(print('É um triangulo escaleno')) 
    
    else:
        str(print('É um triangulo isoceles'))
        
    
    print()    
        
    
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break 