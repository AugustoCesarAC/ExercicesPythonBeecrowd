# -*- coding: utf-8 -*-
"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.



@author: AC
"""

#1060
i = 0
u = 0
lst = []
while i < 6:
    a = float(input())
    lst.append(a)
    i += 1
for x in lst:
    if x > 0:
        u +=1
print(str(u) + " valores positivos")