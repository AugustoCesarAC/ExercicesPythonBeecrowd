# -*- coding: utf-8 -*-
"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.



@author: AC
"""

#1046

a, b = map(int,input().split())

h = (24-a)+b

if (h > 24):
    h = h - 24
    
print ("O JOGO DUROU " +str(h)+ " HORA(S)")