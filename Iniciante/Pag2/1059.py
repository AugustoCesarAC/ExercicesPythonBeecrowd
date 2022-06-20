# -*- coding: utf-8 -*-
"""
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

@author: AC
"""

#1059a

i = 1
lst = []
while i <= 100: 
    lst.append(i)
    i += 1
for x in lst:
    if x%2 == 0:
        print(x)

# =============================================================================
# #1059b
#    
# i = 1
# lst = []
# while i <= 100: 
#     lst.append(i)
#     i += 1
# for x in range(len(lst)):
#     if lst[x]%2 == 0:
#         print(lst[x])     
# =============================================================================
