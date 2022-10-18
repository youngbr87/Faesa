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
print('Pesquisa sobre tecnologia')
print(linha)
print('')

#Listas das respostas
respostas = list()
opcoeslpf = ['[1] - Java', '[2] - PHP', '[3] - Python', '[4] - HTML']
opcoesbancdad = ['[1] - MYSQL', '[2] - MongoDB', '[3] - SQL SERVER', '[4] - Oracle']
opcoesfront = ['[1] - HTML5', '[2] - Java Script', '[3] - CSS', '[4] - React']
opcoeside = ['[1] - VS Code', '[2] - Atom', '[3] - X Code', '[4] - Notepad ++']
opcoesusaso = ['[1] - Windows', '[2] - macOS', '[3] - Mint', '[4] - ReactOS']


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
    print('Escolha uma das opções qual sua linguagem de programação favorita? \n')
    i = 0 
    for item in opcoeslpf:
       print(item)  
    print()   
    lpf = int(input('Digite uma das opções: '))
    print()
    #pergunta2
    print('Se tratando de banco de dados qual você mais gosta de usar? \n')
    i = 0 
    for item in opcoesbancdad:
       print(item)  
    print()
    bancdad = int(input('Digite uma das opções: '))
    print()
    #pergunta3
    print('Qual linguagem de front-end você ainda não tem muito dominio?\n')
    i = 0 
    for item in opcoesfront:
       print(item)
    print()
    front = int(input('Digite uma das opções: '))
    print()
    #pergunta4
    print('Sabemos que hoje existem IDE que interpretam diferentes codigos, em qual você prefere codar?\n')
    i = 0 
    for item in opcoeside:
       print(item)
    print()
    ide = int(input('Digite uma das opções: '))
    print()  
    #pergunta5
    print('Queremos saber agora qual SO você prefere para programar?\n')
    i = 0 
    for item in opcoesusaso:
       print(item)
    print()
    usaso = int(input('Digite uma das opções: '))
    print(linha2)
    
    #Apendice das perguntas
    respostas.append([nome, idade, curso, periodo, lpf, bancdad, front, ide, usaso])
    
    #Finalizar
    resp = str(input('Deseja continuar? [S]/[N] => ')) 
    if resp in 'N,n':
           break 

#Print das repostas
print('-=' *40)
print (f'{"No.":<5}{"NOME":<15}{"IDADE":<15}{"CURSO":<15}{"PERIODO":<15}')
for i, a in enumerate(respostas):
    print(f'{i:<5}{a[0]:<15}{a[1]:<15}{a[2]:<15}{a[3]:<15}')
print()
print()    
print(f'{"BACK-END":<15}{"BANCO":<15}{"FRONT-END":<15}{"IDE":<15}{"SO":<15}')
for i, a in enumerate(respostas):
    print(f'{opcoeslpf[a[4] - 1]:<15}{opcoesbancdad[a[5] - 1]:<15}{opcoesfront[a[6] - 1]:<15}{opcoeside[a[7] - 1]:<15}{opcoesusaso[a[8] - 1]:<15}') 
print()
#Abaixo através dos resultados dos vetores foi calculado os resultados
print('-=' *40)
print()
print('APURAÇÃO DE RESULTADOS')
print()
print('Back end')
#print('Java = ') f'{opcoeslpf}

