#Autor: Vinicius Salles
#Exercicio do curso de logica UDEMY
#Foi feito primeiro no visualg


from ast import While


str(print('-------------------------------'))
str(print('      Exercicio senha          '))
str(print('-------------------------------'))
print()

while True:
    senha = int(input('Digite a senha => '))
    print() 
    x = 2002

    if x == senha:
        str(print('BEM VINDO!'))
        break
        
    else:
        str(print('ACESSO NEGADO'))
        
        
        