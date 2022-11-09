#Exercicio do curso da udemy
#Exercicio feito em visualg
#Programa segundos

while True:

    duracao = int(input('Digite a quantidade de segundos => '))

    horas = duracao // 3600
    resto = duracao % 3600
    minutos = resto // 60
    segundos = resto % 60

    str(print(horas,':',minutos,':',segundos))
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break

