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

#Listas das respostas
respostas = list()
opcoesesportes = ['[1] - FUTEBOL', '[2] - VOLEI', '[3] - BASQUETE', '[4] - CICLISMO', '[5] - HANDBALL', '[6] - BEACH TENIS']
opcoessemana = ['[1] - 1 X NA SEMANA', '[2] - 2 X NA SEMANA', '[3] - 3 X NA SEMANA', '[4] - 4 X NA SEMANA', '[5] - 5 X NA SEMANA OU MAIS']



while True:
    nome = str(input('Qual é o seu nome? '))
    print('\n')
    idade = input('Qual sua idade? ')
    print('\n')
    curso = str(input('Qual curso que você está fazendo? '))
    print('\n')
    periodo = input('Em qual periodo você está? ')
    print()
    print(linha2)
    print()
    #pergunta1
    print('Qual seu esporte favorito ? \n')
    i = 0 
    for item in opcoesesportes:
       print(item)  
    print()   
    esporte = int(input('Digite uma das opções: '))
    print()
    #pergunta2
    print('Quantas vezes você pratica na semana? \n')
    i = 0 
    for item in opcoessemana:
       print(item)  
    print()
    semana = int(input('Digite uma das opções: '))
    print()
    
     #Apendice das perguntas
    respostas.append([nome, idade, curso, periodo, esporte, semana])
    
    #Finalizar
    resp = str(input('Deseja continuar? [S]/[N] => ')) 
    if resp in 'N,n':
           break 

#Print das repostas
print('-=' *40)
print (f'{"No.":<5}{"NOME":<15}{"IDADE":<15}{"CURSO":<15}{"PERIODO":<15}{"ESPORTE":<15}{"FREQUENCIA":<15}')
for i, a in enumerate(respostas):
    print(f'{i:<5}{a[0]:<15}{a[1]:<15}{a[2]:<15}{a[3]:<15}{opcoesesportes[a[4] - 1]:<15}{opcoessemana[a[5] - 1]:<15}')

print()
#Abaixo através dos resultados dos vetores foi calculado os resultados
print('-=' *50)
print()
print('APURAÇÃO DE RESULTADOS')
print()
print('Back end')
#print('Java = ') f'{opcoeslpf}

