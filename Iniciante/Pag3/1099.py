# -*- coding: utf-8 -*-
"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.



@author: AC
"""

#1099
casoTest = int(input())
iterator = 0
iteratorFor = 0
while iterator < casoTest:
    somaImpar = 0
    rangeA, rangeB = map(int,input().split())
    if rangeA > rangeB: num_odd = [num for num in range(rangeB+1,rangeA) if num%2 != 0]
    else: num_odd = [num for num in range(rangeA+1,rangeB) if num%2 != 0]
    for iteratorFor in num_odd:
        somaImpar += iteratorFor
    print(somaImpar)
    iterator += 1