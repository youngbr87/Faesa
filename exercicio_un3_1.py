#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
while True:
    print('-----------------------------------')
    print('   ATENDIMENTO CLASSIFICACAO 2.0   ')
    print('-----------------------------------')
    print()
    nome = input('Digite o nome do paciente: ')
    print()
    idade = int(input('Digite a idade do paciente: '))
    print()
    infec = input('Suspeita de doenca contagiosa [S]/[N]').upper()
    print()
    if idade >= 65:
        print('============================')
        print('  ATENDIMENTO PRIORITARIO   ')
        print('============================')
        if infec == 'S':
            print('Encaminhe paciente para sala AMARELA')
        elif infec == 'N':
            print('Encaminhe paciente para sala BRANCA')
        else:
            print('Responda a suspeita de doença infectocontagiosa com [S]/[N] =>')    
    
    else:
        print('==============================')
        print('  ATENDIMENTO SEM PRIORIDADE  ')
        print('===============================')
        if infec == 'S':
            print('Encaminhe paciente para sala AMARELA')
        elif infec == 'N': 
            print('Encaminhe paciente para sala BRANCA')
        else:
            print('Responda a suspeita de doença infectocontagiosa com [S]/[N]')
               
    print()            
    resp = str(input("Deseja continuar ? [S]/[N] ")).upper()
    if resp == 'N':
        break