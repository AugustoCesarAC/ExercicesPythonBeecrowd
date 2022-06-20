# -*- coding: utf-8 -*-
"""
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo



@author: AC
"""


#1096

i = 1
j = 7

while i <= 9:
    while j > 5:
        print("I={0} J={1}".format(i,j))
        j -= 1
    print("I={0} J={1}".format(i,j))
    i += 2
    j += 2