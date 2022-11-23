#coding: utf-8

#Programa de pesquisas
#Desenvolvido por: Vinicius Salles
#Curso: TADS
#1 Periodo
#Orientadora: Renata Laranja
#Faesa
#Data de criação 18 de agosto de 2022
#Versao 1.0

'''
Objetivo do programa: explorar estruturas básicas para o desenvolvimento de um programa
e ambientação com a linguagem.
'''
from ast import main
from calendar import c
from ctypes.wintypes import LPFILETIME
import string

    
linha = '==========================='
linha2 = '--------------------------------------------------------------'
print()
print(linha)
print('Pesquisa ESPORTES')
print(linha)
print('')

esporte = ['beach tenis']
semana = ['2 X NA SEMANA']

#Listas das respostas
respostas = list()
opcoesesportes = ['[1] - FUTEBOL', '[2] - VOLEI', '[3] - BASQUETE', '[4] - CICLISMO', '[5] - HANDBALL', '[6] - OUTRO']
opcoessemana = ['[1] - 1 X NA SEMANA', '[2] - 2 X NA SEMANA', '[3] - 3 X NA SEMANA', '[4] - 4 X NA SEMANA', '[5] - 5 X NA SEMANA OU MAIS']


while True:
   print('''
   0 - Entrar no programa
   1 - Cadastrar esporte.
   2 - Mostrar dados da lista.
   3 - Remover dados da lista.
      ''')
   
   opcaomenu = int(input('Digite a opção desejada: '))
   if opcaomenu==0:
      #pergunta1
      print('Qual seu esporte favorito ? \n')
      i = 0 
      for item in opcoesesportes:
         print(item)  
      print()   
      esporte = int(input('Digite uma das opções: '))
      if esporte==6:
         opcoesesportes[1]=str(input('Qual é o esporte -> '))
      print()
      #pergunta2
      print('Quantas vezes você pratica na semana? \n')
      i = 0 
      for item in opcoessemana:
         print(item)  
      print()
      semana = int(input('Digite uma das opções: '))
      print()
   elif opcaomenu==1:
      opcoesesportes.append(str(input('Digite o nome do esporte => ')))
   elif opcaomenu==2:
      print('')
      print('Essa são as suas listas:{}-{}'.format(esporte,semana)) 
   elif opcaomenu==3:
            print('DADOS ARMAZENADOS{}'.format(esporte,semana))
            opcoesesportes = int(input('Digite o numero do esporte que deseja remover: '))
            opcoesesportes-=1
            esporte[opcoesesportes]="#"
                  
   respostas.append([esporte, semana])

   #Finalizar
   resp = str(input('Voltar para o menu? [S]/[N] => ')) 
   if resp in 'N,n':  
      break     
