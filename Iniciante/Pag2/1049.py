# -*- coding: utf-8 -*-
"""
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.



Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.



@author: AC
"""

# 1049
a = str(input())
b = str(input())
c = str(input())

an = ["vertebrado", "invertebrado"]
an_2 = ["ave","mamifero","inseto","anelideo"]
an_ver = ["onivoro","herbivoro","carnivoro"]
an_inv = ["hematofago","herbivoro","onivoro"]

an_f = ["pomba","aguia","homem","vaca","pulga","lagarta","sanguessuga","minhoca"]

i = 0

if a == an[0]: 
    i = i + 1
    if b == an_2[0]: 
        i = i + 1        
    else:  
        i = i + 3
    if c == an_ver[0]: 
        i = i + 1
    else: 
        i = i + 2
        
elif a == an[1]: 
    i = i + 5
    if b == an_2[2]:
        i = i + 1
    else:
        i = i + 3
    if c == an_inv[0]:
        i = i + 1
    else: 
        i = i + 2
    
i = i -3

print(an_f[i])