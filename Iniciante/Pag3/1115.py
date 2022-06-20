# -*- coding: utf-8 -*-
"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

@author: AC
"""

#1115
while True:
    x, y = map(float,input().split())

    ponto_list = ["primeiro", "segundo", "terceiro", "quarto"]

    if (x > 0 and y > 0): print(ponto_list[0])
    elif (x < 0 and y > 0): print(ponto_list[1])
    elif (x < 0and y < 0): print(ponto_list[2])
    elif (x > 0 and y < 0): print(ponto_list[3])
    elif (x == 0 or y == 0): break