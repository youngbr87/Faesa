#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#if elif else
#Lista 5
#Exercicio 6

while True:
    
    str(print('---------------------------'))
    str(print('       Nota de aluno       '))
    str(print('---------------------------'))
    print()
    nome = str(input('Digite o nome do aluno => '))
    n_trab = float(input('Digite a nota do trablho => '))
    n_prov = float(input('Digite a nota da prova => '))
    
    media = (n_prov + n_trab) / 2
    
    print()
    
    if media > 7:
        str(print('O aluno', nome, 'está aprovado'))
    else:    
        str(print('O aluno', nome, 'está reprovado'))
    print()
    resp = str(input('Deseja continuar ? [S]/[N] => '))
    if resp in 'N,n':
        break