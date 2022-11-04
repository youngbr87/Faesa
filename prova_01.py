str(print('-----------------------------'))
str(print('      PROVA DE ALUNO         '))
str(print('-----------------------------'))


c = media = nota_1 = nota_2 = 0 

for c in range(0,20):
    mat = int(input('Digite a matricula do aluno => '))
    nota_1 = float(input('Digite a nota 1 => '))
    nota_2 = float(input('Digite a nota 2 => '))
    media = (nota_1 + nota_2) / 2
    if media < 5:
      str(print('O aluno está REPROVADO'))
    elif media < 7:
      str(print('O aluno está RECUPERAÇÃO'))
    else:
        str(print('O aluno está APROVADO!!!'))
    
