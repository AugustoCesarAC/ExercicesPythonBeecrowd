# -*- coding: utf-8 -*-
"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.



@author: AC
"""

#1043

a, b, c = map(float,input().split())

bc = abs(b-c)
ac = abs(a-c)
ab = abs(a-b)

if (bc < a) and (a < b+c) and (ac < b) and (a < a+c) and (ab < c) and (c < b+a):
    p = a+b+c
    print ("Perimetro = %.1f" %p)
else:
    area = ((a+b)*c)/2
    print("Area = %.1f" %area)