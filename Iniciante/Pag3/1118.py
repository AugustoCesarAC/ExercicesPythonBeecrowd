# -*- coding: utf-8 -*-
"""
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

Entrada
O arquivo de entrada contém vários valores reais, positivos ou negativos. Quando forem lidas duas notas válidas, deve ser lido um valor inteiro X . O programa deve parar quando o valor lido para este X for igual a 2.

Saída
Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” seguido do valor do cálculo.

Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e esta mensagem deve ser apresentada novamente se o valor da entrada padrão para X for menor do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.



@author: AC
"""

#1118

nota_soma = 0 
cont = 0
continuar = True

while continuar==True:
  nota = float(input())
  
  if nota>=0.0 and nota <=10:
    nota_soma += nota
    cont += 1 

    if cont == 2:
      
      print("media = %.2f"%(nota_soma/2))
      cont = 0 
      nota_soma = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
          continuar = False
          break
        elif novo == 1:
          continuar = True
          break
      
  else:
    print("nota invalida")