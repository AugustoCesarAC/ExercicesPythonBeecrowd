# -*- coding: utf-8 -*-
"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.



@author: AC
"""

# 1038
preco_list = [4.00, 4.50, 5.00, 2.00, 1.50]

cod, quant = map(int,input().split())
    
valor_final = preco_list[cod-1]*quant
print("Total: R$ %.2f" %valor_final)