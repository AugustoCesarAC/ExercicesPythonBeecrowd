# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:07:43 2022

@author: AC
"""
# 1037
# =============================================================================
# valor = float(input())
# 
# valor_list = [0,25,50,75,100]
# 
# i = 0
# 
# if (valor < 0) or (valor > 100):
#     print ("Fora de intervalo")
# else:
#     for x in valor_list:
#                 
#         if (valor > valor_list[i]) and (valor <= valor_list[i+1]) or (valor == valor_list[i]) and (valor == 0):
#             if (valor == 0):
#                 print ("Intervalo [" + str(valor_list[0]) + "," + str(valor_list[1]) + "]")
#             elif (valor <= 25):  
#                 print ("Intervalo [" + str(valor_list[0]) + "," + str(valor_list[1]) + "]")
#             elif (valor == valor_list[i]):
#                 print ("Intervalo (" + str(valor_list[i-1]) + "," + str(valor_list[i]) + "]")     
#             else:
#                 print ("Intervalo (" + str(valor_list[i]) + "," + str(valor_list[i+1]) + "]")   
#       
#         i = i + 1
# =============================================================================     
            
# =============================================================================
# 1038
# preco_list = [4.00, 4.50, 5.00, 2.00, 1.50]
# 
# cod, quant = map(int,input().split())
#     
# valor_final = preco_list[cod-1]*quant
# print("Total: R$ %.2f" %valor_final)
# =============================================================================
    
# =============================================================================
# 1040
# a, b, c, d = map(float,input().split())
# 
# media = ((a*2)+(b*3)+(c*4)+(d*1))/10
# 
# print ("Media: %.1f" %media)
# 
# if (media >= 7): print ("Aluno aprovado.")
# 
# elif (media >= 5) and (media < 7): 
#     print ("Aluno em exame.")
#     exame = float(input())
#     media = (exame + media)/2
#     print ("Nota do exame: %.1f" %exame)
#     if (media >= 5): 
#         print("Aluno aprovado.")
#         print("Media final: %.1f" %media)
#     else: print("Aluno reprovado.")
# else: print ("Aluno reprovado.")
# =============================================================================

# =============================================================================
# #1041
# 
# x, y = map(float,input().split())
# 
# ponto_list = ["Q1", "Q2", "Q3", "Q4", "Origem", "Eixo X", "Eixo Y"]
# 
# if (x > 0and y > 0): print(ponto_list[0])
# elif (x < 0 and y > 0): print(ponto_list[1])
# elif (x < 0and y < 0): print(ponto_list[2])
# elif (x > 0 and y < 0): print(ponto_list[3])
# elif (x == 0 and y == 0): print(ponto_list[4])
# elif ((x > 0 or x < 0) and y == 0): print(ponto_list[5])
# elif ((y > 0 or y < 0) and x == 0): print(ponto_list[6])
# =============================================================================

# =============================================================================
# #1042
# 
# lista = []
# 
# a, b, c = map(int,input().split())
# 
# lista.append(a)
# lista.append(b)
# lista.append(c)
# 
# lista.sort(reverse=True)
# 
# print(lista[2]), print(lista[1]), print(lista[0])
# 
# print("")
# 
# print(a), print(b), print(c)
# =============================================================================

# =============================================================================
# #1043
# 
# a, b, c = map(float,input().split())
# 
# bc = abs(b-c)
# ac = abs(a-c)
# ab = abs(a-b)
# 
# if (bc < a) and (a < b+c) and (ac < b) and (a < a+c) and (ab < c) and (c < b+a):
#     p = a+b+c
#     print ("Perimetro = %.1f" %p)
# else:
#     area = ((a+b)*c)/2
#     print("Area = %.1f" %area)
# =============================================================================

# =============================================================================
# #1044
# 
# a, b = map(int,input().split())
# 
# if (b%a == 0) or (a%b == 0):
#     print("Sao Multiplos")
# else:
#     print("Nao sao Multiplos")
# =============================================================================



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    