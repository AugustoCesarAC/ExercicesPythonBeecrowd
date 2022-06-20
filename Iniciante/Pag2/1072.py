# -*- coding: utf-8 -*-
"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.



@author: AC
"""

#1072
i = int(input())
u = 0
lst = []
while u < i:
    a = int(input())
    lst.append(a)
    u += 1

numIn = 0
numOut = 0

for x in lst:
    if x in range(10,21): numIn += 1
    else: numOut += 1
    
print(str(numIn)+ " in")
print(str(numOut)+ " out")
        