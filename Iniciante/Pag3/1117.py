# -*- coding: utf-8 -*-
"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

Entrada
A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

Saída
Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.


@author: AC
"""

#1117
media = None
notaList = []
while media == None:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        notaList.append(nota)
        if len(notaList) == 2:
            media = (notaList[0]+notaList[1])/2
            print("media = %.2f" %media)
    else:
        print("nota invalida")