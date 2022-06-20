# -*- coding: utf-8 -*-
"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

@author: AC
"""

cp1,pn1,vp1 = map(float,input().split())
cp2,pn2,vp2 = map(float,input().split())

vl1 = pn1*vp1
vl2 = pn2*vp2
vlf = vl1+vl2

print ('VALOR A PAGAR: R$ {:.2f}'.format(vlf))