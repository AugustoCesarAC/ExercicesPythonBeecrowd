# -*- coding: utf-8 -*-
"""
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.



@author: AC
"""

#1094

qntTest = int(input())
listaCobaia = []
i = 0
totalCobaia = 0
totalCoelho = 0
totalRato = 0
totalSapo = 0
while i < qntTest:
    numCobaia, tipoCom = input().split()
    i +=1
    numCobaia = int(numCobaia)
    listaCobaia.append((numCobaia,tipoCom))

for x in listaCobaia:
    totalCobaia += x[0]
    if x[1] == "C": totalCoelho += x[0]
    if x[1] == "R": totalRato += x[0]
    if x[1] == "S": totalSapo += x[0]
print("Total: "+ str(totalCobaia )+ " cobaias")
print("Total de coelhos: "+ str(totalCoelho))
print("Total de ratos: "+ str(totalRato))
print("Total de sapos: "+ str(totalSapo))

print("Percentual de coelhos: %.2f" %((totalCoelho/totalCobaia)*100) + " %")
print("Percentual de ratos: %.2f" %((totalRato/totalCobaia)*100) + " %")
print("Percentual de sapos: %.2f" %((totalSapo/totalCobaia)*100) + " %")
