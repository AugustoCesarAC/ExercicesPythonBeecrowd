# -*- coding: utf-8 -*-
"""
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada
O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída
Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.



@author: AC
"""

#1079
i = int(input())
u = 0
lst = []
while u < i:
    a, b, c = map(float,input().split())
    a = a*2
    b = b*3
    c = c*5
    media = (a+b+c)/10
    lst.append(media)
    u +=1    
for x in lst: print("%.1f"%x)