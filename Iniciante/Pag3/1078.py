# -*- coding: utf-8 -*-
"""
Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N

Entrada
A entrada contém um valor inteiro N (2 < N < 1000).

Saída
Imprima a tabuada de N, conforme o exemplo fornecido.



@author: AC
"""

#1078
a = int(input())
lst = [num for num in range(1,11)]

for x in lst: print("{0} x {1} = {2}".format(x, a, x*a))