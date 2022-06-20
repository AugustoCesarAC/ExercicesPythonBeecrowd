# -*- coding: utf-8 -*-
"""
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:




Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.



@author: AC
"""

#1050

a = int(input())
n = "DDD nao cadastrado"
i = 0
lst_ddd = [61,71,11,21,32,19,27,31]
lst_des = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

for x in lst_ddd:
    if a == lst_ddd[i]:
        print(lst_des[i])
        break
    else:i = i +1
if i > 7: print(n)