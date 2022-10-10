#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto
#if elif else
while True:
    print('------------------------------')
    print('   ATENDIMENTO CLASSIFICACAO  ')
    print('------------------------------')
    print()
    nome=input("Nome do paciente: ").upper()
    print()
    idade=int(input("Digite a idade: "))
    print()
    infec=input("Suspeita de doença infecto-contagiosa? [S]/[N] => ").upper()
    print()
    if idade>=65:
        print("O paciente ", nome, " possui atendimento PRIORITARIO!")
    elif infec == 'S':
        print("ATENCAO ! O paciente ", nome, "deve ficar em uma sala RESERVADA")
    else: 
        print("O paciente ", nome, "deve aguardar ser chamado no painel.")    
    print()
    resp = str(input("Deseja continuar ? [S]/[N] "))
    if resp in 'N,n':
        break
             
