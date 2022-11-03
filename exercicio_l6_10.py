#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 10

str(print('---------------------------------'))
str(print('      Votos candidato            '))
str(print('---------------------------------'))


voto = branc = nul = cand1 = cand2 = cand3 = nulo = 0
while voto != -1:
   voto = int(input('Digite canditado deseja votar [1] [2] [3] ou  branco [0]  nulo [4] / [-1] SAIR => '))
   if voto == 1:
       cand1 +=1
   elif voto == 2:
       cand2 +=1    
   elif voto == 3:
       cand3 +=1
   elif voto == 0:
       branc +=1
   elif voto == 4:
       nulo +=1
   else:
       str(print('Resposta errada'))              

str(print('O candidadto 1  recebeu', cand1, 'voto (s)'))
str(print('O candidadto 2  recebeu', cand2, 'voto (s)'))
str(print('O candidadto 3  recebeu', cand3, 'voto (s)'))
str(print('Votos em branco', branc,))
str(print('Votos em nulo', nulo,))