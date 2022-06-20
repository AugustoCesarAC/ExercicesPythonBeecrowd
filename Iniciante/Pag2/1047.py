# -*- coding: utf-8 -*-
"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .


@author: AC
"""

#1047
a, b, c, d = map(int,input().split())

h = (24-a)+c
m = (d-b)

if (m < 0):
    m = m + 60

if (h > 24):
    h = h - 24

if (a == c and b < d):
    h = h - 24

if (b > d):
    h = h - 1
    
print ("O JOGO DUROU " + str(h) + " HORA(S) E " + str(m) + " MINUTO(S)")
