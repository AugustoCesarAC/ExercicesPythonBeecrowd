# -*- coding: utf-8 -*-
"""
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

Entrada
A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

Saída
Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.
@author: AC
"""

#1113

while True:
    num1, num2 = map(int,input().split())
    if num1 > num2: print("Decrescente")
    elif num2 > num1: print("Crescente")
    elif num1 == num2: break