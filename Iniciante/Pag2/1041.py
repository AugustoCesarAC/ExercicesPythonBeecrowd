# -*- coding: utf-8 -*-
"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.


@author: AC
"""

#1041

x, y = map(float,input().split())

ponto_list = ["Q1", "Q2", "Q3", "Q4", "Origem", "Eixo X", "Eixo Y"]

if (x > 0and y > 0): print(ponto_list[0])
elif (x < 0 and y > 0): print(ponto_list[1])
elif (x < 0and y < 0): print(ponto_list[2])
elif (x > 0 and y < 0): print(ponto_list[3])
elif (x == 0 and y == 0): print(ponto_list[4])
elif ((x > 0 or x < 0) and y == 0): print(ponto_list[5])
elif ((y > 0 or y < 0) and x == 0): print(ponto_list[6])