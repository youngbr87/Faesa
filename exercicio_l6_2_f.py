#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 2



from tkinter import N


str(print('----------------------'))
str(print('      Fatorial        '))
str(print('----------------------'))

n = int(input('Digite um numero para calcular seu fatorial => '))
c = n
f = 1
print('Calculando {}! =  '.format(n), end='')

for c in range(1, n+1):
    #print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c + 1

str(print('{}'.format(f)))   