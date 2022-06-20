# -*- coding: utf-8 -*-
"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

@author: AC
"""

from decimal import*  
getcontext().prec = 4    
nota = " nota(s) de R$ "
moeda = " moeda(s) de R$ "
dinheiro = Decimal(input())

coringa = 0

nota_list = [100, 50, 20, 10, 5, 2]
moeda_list = list(map(Decimal, [1 ,0.50, 0.25, 0.10, 0.05, 0.01]))

i = 0
print("NOTAS:")
while i < len(nota_list):
    if i == i:
        coringa = int(dinheiro/nota_list[i])
        print(str(coringa) + nota + "%.2f" %nota_list[i])        
        dinheiro = Decimal(dinheiro - (nota_list[i]*coringa))
        i = i+1

im = 0
coringam = 0
print("MOEDAS:")
while im < len(moeda_list):
    if im == im:
        coringam = int(dinheiro/moeda_list[im])
        print(str(coringam) + moeda + "%.2f" %moeda_list[im])
        dinheiro = Decimal(dinheiro - (moeda_list[im]*coringam))
        im = im + 1