# -*- coding: utf-8 -*-
"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

@author: AC
"""

seg = int(input())  

tempo = ""

tempo_list = [3600, 60, 1]
for x in tempo_list:
    
    timing = int(seg / x)
    
     
    if x == 1:
        tempo = tempo + str(timing) 
    else:
        tempo = tempo + str(timing) + ":"

    seg = seg - (x*timing)

print (tempo)