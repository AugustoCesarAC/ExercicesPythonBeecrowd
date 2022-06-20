# -*- coding: utf-8 -*-
"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

@author: AC
"""

a, b, c = map(float, input().split()) 

deltat = (b**2)-(4*a*c)

if a == 0 or deltat < 0:
    print("Impossivel calcular")
else:
    delta = deltat**0.5
    
    r1 = ((b*-1) + delta) / (2*a)
    r2 = ((b*-1) - delta) / (2*a)
    
    print("R1 = %.5f" %r1)
    print("R2 = %.5f" %r2)