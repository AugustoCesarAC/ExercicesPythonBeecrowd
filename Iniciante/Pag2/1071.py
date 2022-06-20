# -*- coding: utf-8 -*-
"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.



@author: AC
"""

#1071
a = int(input())
b = int(input())
y = 0
if a < b: num_odd = [num for num in range(a+1,b) if num % 2 != 0]
else : num_odd = [num for num in range(b+1,a) if num % 2 != 0]
for x in num_odd: 
    y = y + x 

print(y)