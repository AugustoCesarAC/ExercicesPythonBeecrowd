# -*- coding: utf-8 -*-
"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.


@author: AC
"""

#1101
rangeA, rangeB = map(int,input().split())
while rangeA > 0 and rangeB > 0:
    somaGeral = 0
    finalPrint = ""
    if rangeA > rangeB: num_odd = [num for num in range(rangeB,rangeA+1)]
    else: num_odd = [num for num in range(rangeA,rangeB+1)]
    for iteratorFor in num_odd:
        somaGeral += iteratorFor
        finalPrint += str(iteratorFor) + " "
    print(str(finalPrint) + "Sum=" +str(somaGeral))
    rangeA, rangeB = map(int,input().split())