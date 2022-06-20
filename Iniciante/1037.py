# -*- coding: utf-8 -*-
"""
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.

@author: AC
"""

valor = float(input())

valor_list = [0,25,50,75,100]

i = 0

if (valor < 0) or (valor > 100):
    print ("Fora de intervalo")
else:
    for x in valor_list:
                
        if (valor > valor_list[i]) and (valor <= valor_list[i+1]) or (valor == valor_list[i]) and (valor == 0):
            if (valor == 0):
                print ("Intervalo [" + str(valor_list[0]) + "," + str(valor_list[1]) + "]")
            elif (valor <= 25):  
                print ("Intervalo [" + str(valor_list[0]) + "," + str(valor_list[1]) + "]")
            elif (valor == valor_list[i]):
                print ("Intervalo (" + str(valor_list[i-1]) + "," + str(valor_list[i]) + "]")     
            else:
                print ("Intervalo (" + str(valor_list[i]) + "," + str(valor_list[i+1]) + "]")   
      
        i = i + 1