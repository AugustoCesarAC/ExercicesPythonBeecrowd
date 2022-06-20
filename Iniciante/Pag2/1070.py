# -*- coding: utf-8 -*-
"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.



@author: AC
"""

#1070
num_in = int(input())
num_odd = [print(num) for num in range(num_in,num_in+12) if num % 2 != 0]