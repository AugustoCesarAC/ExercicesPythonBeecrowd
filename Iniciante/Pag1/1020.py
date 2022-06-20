# -*- coding: utf-8 -*-
"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

@author: AC
"""

tex = ""  
ano = " ano(s)"
mes = " mes(es)"
diatex = " dia(s)"

dia = int(input())

dia_list = [365, 30, 1]
for x in dia_list:
    
    rest = int( dia / x )
    
    if x == 365:
        tex = str(rest) + ano
    elif x == 30:
        tex = str(rest) + mes 
    else:
        tex = str(rest) + diatex 
    
    dia = dia - (x*rest)
    
    print(tex)