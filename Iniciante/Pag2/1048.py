# -*- coding: utf-8 -*-
"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	Percentual de Reajuste
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

@author: AC
"""

#1048
a = float(input())

lista_salary = []
lista_reajuste = [15, 12, 10, 7, 4]

lista_salary.append((0, 400))
lista_salary.append((400.01,800))
lista_salary.append((800.01,1200))
lista_salary.append((1200.01,2000))
lista_salary.append((2000.01,9999999999))

for x in range(len(lista_salary)):
    if (lista_salary[x][1] >= a and lista_salary[x][0] <= a):
        
        reaju = a*(lista_reajuste[x]/100)
        print("Novo salario: %.2f" %(reaju+a))
        print("Reajuste ganho: %.2f" %reaju)
        print("Em percentual: " + str(lista_reajuste[x]) + " %")
        break