# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:59:34 2022

@author: AC
"""
# =============================================================================
# #1045
# 
# a,b,c = map(float,input().split())
# 
# lista = [a,b,c]
# lista.sort(reverse=True)
# 
# a = lista[0]**2
# b = lista[1]**2
# c = lista[2]**2
# 
# if(lista[0] >= lista[1] + lista[2]):  print("NAO FORMA TRIANGULO")
#     
# elif(a == b+c): print("TRIANGULO RETANGULO")
# elif(a > b+c):  print("TRIANGULO OBTUSANGULO")
# elif(a < b+c):  print("TRIANGULO ACUTANGULO")
# 
# if(a == b == c): print("TRIANGULO EQUILATERO")
# 
# elif(a == b or b == c or c == a): print("TRIANGULO ISOSCELE0S")
# =============================================================================

# =============================================================================
# #1046
# 
# a, b = map(int,input().split())
# 
# h = (24-a)+b
# 
# if (h > 24):
#     h = h - 24
#     
# print ("O JOGO DUROU " +str(h)+ " HORA(S)")
# =============================================================================
    
# =============================================================================
# #1047
# a, b, c, d = map(int,input().split())
# 
# h = (24-a)+c
# m = (d-b)
# 
# if (m < 0):
#     m = m + 60
# 
# if (h > 24):
#     h = h - 24
# 
# if (a == c and b < d):
#     h = h - 24
# 
# if (b > d):
#     h = h - 1
#     
# print ("O JOGO DUROU " + str(h) + " HORA(S) E " + str(m) + " MINUTO(S)")
# =============================================================================

# =============================================================================
# #1048
# 
# a = float(input())
# 
# lista_salary = []
# lista_reajuste = [15, 12, 10, 7, 4]
# 
# lista_salary.append((0, 400))
# lista_salary.append((400.01,800))
# lista_salary.append((800.01,1200))
# lista_salary.append((1200.01,2000))
# lista_salary.append((2000.01,9999999999))
# 
# for x in range(len(lista_salary)):
#     if (lista_salary[x][1] >= a and lista_salary[x][0] <= a):
#         
#         reaju = a*(lista_reajuste[x]/100)
#         print("Novo salario: %.2f" %(reaju+a))
#         print("Reajuste ganho: %.2f" %reaju)
#         print("Em percentual: " + str(lista_reajuste[x]) + " %")
#         break
# =============================================================================

#1049
        














                