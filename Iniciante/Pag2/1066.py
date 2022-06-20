# -*- coding: utf-8 -*-
"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.



@author: AC
"""

#1066

i = 0
par = 0
impar = 0
pos = 0
neg = 0
lst = []
while i < 5:
    a = int(input())
    lst.append(a)
    i += 1
for x in lst:
    if x%2 == 0: par +=1
    if x%2 != 0: impar +=1
    if x>0: pos +=1
    if x<0: neg +=1
        
print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(pos) + " valor(es) positivo(s)")
print(str(neg) + " valor(es) negativo(s)")