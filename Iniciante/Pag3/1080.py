# -*- coding: utf-8 -*-
"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.



@author: AC
"""

#1080

u = 0
lst = []
x1 = 0
x2 = 0
while u < 100:
    a = int(input())
    lst.append(a)
    u +=1    
for x in lst:
    if x > x1:
        x1 = x
        x2 = lst.index(x)
print("{0}\n{1}".format(x1,x2+1))