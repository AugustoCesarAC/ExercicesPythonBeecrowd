# -*- coding: utf-8 -*-
"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.



@author: AC
"""

#1098

i = 0
j = 1
z = 3
lst = []
while i < 2:
    contador = 0
    while contador <= 2:
        if round(i,1) == 1.0:
            i = int(i)
            j = int(j)
            print("I={0} J={1}".format(i,j))
        elif i >= 1.9: 
            i = int(2)
            j = int(j)
            print("I={0} J={1}".format(i,j))
        else:
            print("I={0} J={1}".format(round(i,1),round(j,1)))
        j += 1
        contador += 1
    i += 0.2
    j -= 2.8
    z += 0.2