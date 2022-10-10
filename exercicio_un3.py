#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional simples

from ast import If

while True:
    print("--------------------------")
    print("  PRIORIDADE ATENDIMENTO  ")
    print("--------------------------")
    print
    nome=input("Digite um nome: ")
    idade=int(input("Digite a idade: "))
    prioridade="NAO"
    if idade>=65:
        prioridade="SIM"
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade) 
    resp = str(input('Deseja continuar [S]/[N] => '))
    if resp in "N,n":    
        break    