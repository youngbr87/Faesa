#exericio unidade 3
#Professora Renata Laranja
#Estrutura de repetiçao
#for while
#Lista Sanca 
#Exercicio 1

str(print('------------------------'))
str(print('          Tabuada       '))
str(print('------------------------'))

while True: 
    n = int(input('Deseja tabuada de qual valor => '))
    print('-' * 30)
    for c in range(1, 11): 
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)    