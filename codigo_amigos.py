#Desenvolvido por: Gabriel Fischer, Gustavo Romão e Wendell Athaides
#Curso: TADS-CI-1014-222-1DC2
#O comanado \033 é para colocar cor na linha e tem um \033 no final para não ficar tudo com aquela cor
import time
#Listas criadas
#Usamos o .format() para formatar os espaços de {}<CHAVES que é basicamente a informação que vai estar dentro delas no print
nomes = ['Domingão Com Huck']
horas = ['17:30']
emissora = ['GLOBO']
#While true no ínicio para ficar reproduzindo o codigo até fechar manualmente no terminal
while True:
#Menu de opções
#O len para ler todos os nomes escritos dentro da lista de nomes(para fazer a pesquisa)
    num = len(nomes)
    print('\033[1;31m--------------- PROGRAMAÇÃO DE TV ---------------\033[m')
    print("""
1- Pesquise o nome da programação desejada.
2- Cadastrar programação.
3- Mostrar todas as programações salvas.
4- Alterar dados da lista.
5- Remover dados da lista.
    """)
#Soliitação da opção desejada e o while para informar opção invalida caso o valor seja diferente dos propostos
    pinteracao = int(input('Digite oque deseja: '))
    while pinteracao!=1 and pinteracao!=2 and pinteracao!=3 and pinteracao!=4 and pinteracao!=5:
        print("""
Opção inválida!""")
        pinteracao = int(input('Digite oque deseja: '))
#OPÇÃO 1 DO MENU
#Pesquisar a programação ja cadastrada, ele le a lista usando o for e o >if< com a condição faz com que encontre o programa cadastrado
#O time.sleep(5) é pra ter um delay de 5segundos dps que mostrar a lista pesquisada(essa função so funciona com o import time feito na >4< linha)
    if pinteracao==1:
        sinteracao = str(input('Digite a programação desejada: '))
        for contador in range(0, num):
            if nomes[contador]==sinteracao:
                print("""\033[1;42mA programação ja foi cadastrada, confira:\033[m
Nome: {}
Horário de ínicio: {}
Emissora: {}
                """.format(nomes[contador],horas[contador],emissora[contador]))
                time.sleep(5)
            else:
                print("""\033[1;41m
Este programa nao está cadastrado!\033[m""")
#OPÇÃO 2 DO MENU
#primeiro ele faz uma pergunta se deseja cadastrar e a pessoa responde com SIM ou NAO, caso seja uma repsosta diferente ela vai entrar no while e vai dar opção invalida.
#ae o primeiro IF é caso a resposta seja 'SIM' ele vai fazer o >append< que é adicionar ao final da lista oque for digitado ali
#caso ele digite 'NAO' vai simplesmente cancelar e voltar pro menu inicial
    elif pinteracao==2:
            print("""Deseja cadastrar uma programação?
            """)
            resposta = str(input('SIM ou NAO: ')).upper()
            while resposta!='SIM' and resposta!='NAO':
                print("""\033[1;31m
Opção Inválida!\033[m""")
                resposta = str(input('SIM ou NAO: ')).upper()
            if resposta=='SIM':
                print("""
Digite as informações requisitadas:""")
                nomes.append(str(input('Digite o nome da programação: ')))
                horas.append(str(input('Digite o horário de ínicio: ')))
                emissora.append(str(input('Digite o nome da emissora: ')))
                print("""
------------------------------
\033[1;32mA programação foi Cadastrada!\033[m
------------------------------
                """)
                time.sleep(2)
            else:
                print("""
------------------------------
A programação foi Cancelada!
------------------------------
                """)
                time.sleep(2)
#OPÇÃO 3 DO MENU
#Simplesmente a printou os vetos e adicionamos o time.sleep(5) para a mesma função ja citada
    elif pinteracao==3:
        print('')
        print("""Essa são as suas listas:
{}
{}
{}
        """.format(nomes,horas,emissora))
        time.sleep(5)
#OPÇÃO 4 DO MENU
#Solicitamos um menu para a pessoa escolher oque ela quer mudar, o while funciona da mesma forma impedindo a pessoa de pesquisar algo diferente do proposto
#Caso ela solicite a opção '1' ela vai fazer o cadastramento de nomes e o >terinteração-=1< funciona para que ele nao escolha a item da lista a partir do numero 0 e sim do numero 1
#A mesma coisa funciona para o 2-horas e 3-emissora é o mesmo sistema
    elif pinteracao==4:
        print("""
Coisas para alterar:
1- Nomes
2- Horas
3- Emissora
        """)
        terinteracao = int(input('Digite oque deseja alterar: '))
        while terinteracao!=1 and terinteracao!=2 and terinteracao!=3:
            print("""\033[1;31m
Opção Inválida!\033[m""")
            terinteracao = int(input('Digite oque deseja alterar: '))
        if terinteracao==1: 
            print("""
Essa são suas programações salvas:
{}
            """.format(nomes))
            terinteracao = int(input('Digite o número da programação que voce deseja alterar: '))
            terinteracao-=1
            nomes[terinteracao]=str(input('Digite o novo nome do programa: '))
            print("""
------------------------------
\033[33mO nome da programação foi alterada para \033[31m{}\033\033[m!
------------------------------
            """.format(nomes[terinteracao]))
            time.sleep(3)
        elif terinteracao==2: 
            print("""
Essa são suas programações salvas:
{}
            """.format(horas))
            terinteracao = int(input('Digite a hora da programação que voce deseja alterar: '))
            terinteracao-=1
            horas[terinteracao]=str(input('Digite o novo horário do programa: '))
            print("""
------------------------------
\033[33mAs horas foram alterada para \033[31m{}\033\033[m!
------------------------------
            """.format(horas[terinteracao]))
            time.sleep(3)
        elif terinteracao==3: 
            print("""
Essa são seus horarios das programações salvas:
{}
            """.format(emissora))
            terinteracao = int(input('Digite o número da programação que voce deseja alterar: '))
            terinteracao-=1
            emissora[terinteracao]=str(input('Digite a nova emissora do programa: '))
            print("""
------------------------------
\033[33mA emissora foi alterada para \033[31m{}\033\033[m!
------------------------------
            """.format(emissora[terinteracao]))
            time.sleep(3)
#OPÇÃO 5 DO MENU
#Ele vai solicitar o nome do programa que deseja remover usando o mesmo sistema de >qinteracao-=1< para começar do primeiro e nao do 0
#Dps de selecionado ele altera o nome,hora,emissora para '#' que é oque a professora quis que usasse.
    elif pinteracao==5:
            print("""
Essa são suas programações salvas:
{}
            """.format(nomes,horas,emissora))
            qinteracao = int(input('Digite o número da programação que voce deseja remover: '))
            qinteracao-=1
            nomes[qinteracao]="#"
            horas[qinteracao]="#"
            emissora[qinteracao]="#"