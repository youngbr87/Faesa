#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 11

str(print('---------------------------'))
str(print('        CALCULO IMC        '))
str(print('---------------------------'))

while True:

    peso = float(input('Digite o peso do paciente => '))
    altura = float(input('Digite a altura do paciente => '))

    imc = peso / (altura * altura)

    if imc <= 20:
        str(print('Abaixo do peso'))
    elif imc <= 25:
        str(print('Peso normal'))
    elif imc <= 35:
        str(print('Exesso de peso'))        
    elif imc <= 50:
        str(print('Obesidade'))
    else:         
        
        resp = str(input('Deseja continuar ? [S]/[N] => '))
        if resp in 'N,n':
          break