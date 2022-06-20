# -*- coding: utf-8 -*-
"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.



@author: AC
"""

#1064
i = 0
u = 0
media = 0
lst = []
while i < 6:
    a = float(input())
    lst.append(a)
    i += 1
for x in lst:
    if x > 0:
        u +=1
        media += x
print(str(u) + " valores positivos")
media = media/u
print("%.1f" %media)