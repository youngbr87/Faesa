#exericio unidade 3
#Professora Renata Laranja
#Desvio de condicional composto e aninhado
#while for
#Lista 6
#Exercicio 10

str(print('---------------------------------'))
str(print('      Votos candidato            '))
str(print('---------------------------------'))

print()

voto = branc = nul = cand1 = cand2 = cand3 = nulo = soma = 0
while voto != -1:
   voto = int(input('Digite canditado deseja votar [1] [2] [3] para branco [0] ou nulo [4] / Digite [-1] SAIR => '))
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
       if voto == -1:
        str(print('Grato.'))
       else:
           str(print('Opção invalida tente novamente ou digite [-1] para sair.'))
           
       
print() 

print('-----------------------------------------------------')          

if cand1 > cand2 and cand1 > cand3:
        str(print('O candidato 1 recebeu mais votos'))
elif cand2 > cand1 and cand2 > cand3:                            
        str(print('O candidato 2 recebeu mais votos'))  
elif cand3 > cand1 and cand3 > cand2:                            
        str(print('O candidato 3 recebeu mais votos')) 
else:
     str(print('EMPATE'))         
        
soma = cand1 + cand2 + cand3 + branc + nulo

print('-----------------------------------------------------')       
        
        
str(print('O candidadto 1  recebeu', cand1, 'voto (s)'))
str(print('O candidadto 2  recebeu', cand2, 'voto (s)'))
str(print('O candidadto 3  recebeu', cand3, 'voto (s)'))

print()
str(print('Votos em branco => ', branc,))
str(print('Votos em nulo => ', nulo,))

print()
str(print('O número total de eleitores foi => ', soma))