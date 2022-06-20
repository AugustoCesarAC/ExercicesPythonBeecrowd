# -*- coding: utf-8 -*-
"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.



@author: AC
"""

#1065
i = 0
u = 0
lst = []
while i < 5:
    a = float(input())
    lst.append(a)
    i += 1
for x in lst:
    if x%2 == 0:
        u +=1
print(str(u) + " valores pares")