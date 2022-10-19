#Autor: Vinicius Salles
#Exercicio do curso de logica UDEMY
#Foi feito primeiro no visualg

str(print('--------------------------------'))
str(print(' Crescente decrescente          '))
str(print('--------------------------------'))

print()
while True:
    num_1 = int(input('Digite um número => '))
    print()
    num_2 = int(input('Digite outro número => '))
    print() 
    while num_1 != num_2:
        if num_1 < num_2:
            str(print('Crescente'))
            break
        else:
            str(print('Decrescente'))
            break
    print()
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break
 

print()
str(print('Obrigado'))
            
        

    
    
