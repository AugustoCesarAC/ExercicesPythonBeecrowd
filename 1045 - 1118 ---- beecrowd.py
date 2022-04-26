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

# =============================================================================
# # 1049
# a = str(input())
# b = str(input())
# c = str(input())
# 
# an = ["vertebrado", "invertebrado"]
# an_2 = ["ave","mamifero","inseto","anelideo"]
# an_ver = ["onivoro","herbivoro","carnivoro"]
# an_inv = ["hematofago","herbivoro","onivoro"]
# 
# an_f = ["pomba","aguia","homem","vaca","pulga","lagarta","sanguessuga","minhoca"]
# 
# i = 0
# 
# if a == an[0]: 
#     i = i + 1
#     if b == an_2[0]: 
#         i = i + 1        
#     else:  
#         i = i + 3
#     if c == an_ver[0]: 
#         i = i + 1
#     else: 
#         i = i + 2
#         
# elif a == an[1]: 
#     i = i + 5
#     if b == an_2[2]:
#         i = i + 1
#     else:
#         i = i + 3
#     if c == an_inv[0]:
#         i = i + 1
#     else: 
#         i = i + 2
#     
# i = i -3
# 
# print(an_f[i])
# =============================================================================
    
# =============================================================================
# #1050
# 
# a = int(input())
# n = "DDD nao cadastrado"
# i = 0
# lst_ddd = [61,71,11,21,32,19,27,31]
# lst_des = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]
# 
# for x in lst_ddd:
#     if a == lst_ddd[i]:
#         print(lst_des[i])
#         break
#     else:i = i +1
# if i > 7: print(n)
# =============================================================================

# =============================================================================
# #1051         
#     
# a = float(input())
# 
# new = 0
# new2 = 0
# joker = 0
# 
# if a <= 2000:
#     print("Isento")
# elif a > 2000 and a <= 3000:
#     a = (a-2000)*0.08
#     print("R$ %.2f"%(a))
# elif a > 3000 and a <= 4500:
#     new = (a - 3000)*0.18
#     a = 1000 * 0.08
#     print("R$ %.2f"%(a + new))
# elif a > 4500:
#     while a > 4500:
#         a = a - 1 
#         joker = joker + 1
#     joker = joker*0.28
#     new = (a - 3000.01)*0.18
#     a = 1000 * 0.08
#     print("R$ %.2f"%(joker + new + a))
# =============================================================================

# =============================================================================
# #1052
# 
# lstMes = ['January','February','March','April','May','June','July','August','September','October','November','December']
# 
# a = int(input())
# 
# print(lstMes[a-1])
# =============================================================================

# =============================================================================
# #1059a
# 
# i = 1
# lst = []
# while i <= 100: 
#     lst.append(i)
#     i += 1
# for x in lst:
#     if x%2 == 0:
#         print(x)
# =============================================================================

# =============================================================================
# #1059b
#    
# i = 1
# lst = []
# while i <= 100: 
#     lst.append(i)
#     i += 1
# for x in range(len(lst)):
#     if lst[x]%2 == 0:
#         print(lst[x])     
# =============================================================================

# =============================================================================
# #1060
# i = 0
# u = 0
# lst = []
# while i < 6:
#     a = float(input())
#     lst.append(a)
#     i += 1
# for x in lst:
#     if x > 0:
#         u +=1
# print(str(u) + " valores positivos")
# =============================================================================

# =============================================================================
# #1061
# 
# dia1 = input().split()
# dia1 = int(dia1[1])
# 
# h1, m1, s1 = map(int,input().split(":"))
# dia2 = input().split()
# dia2 = int(dia2[1])
# h2, m2, s2 = map(int,input().split(":"))
# 
# seg1 = (dia1*86400)+(h1*3600)+(m1*60)+s1
# seg2 = (dia2*86400)+(h2*3600)+(m2*60)+s2
# seg3 = seg2-seg1
# 
# diaF = seg3//86400
# hF = seg3//3600
# while hF >= 24: hF = int(hF - 24)
# 
# mF = seg3//60
# while mF >= 60: mF = int(mF - 60)
#     
# sF = (seg3-(diaF*86400)-(hF*3600)-(mF*60))
# 
# print('%.0f'%diaF + ' dia(s)')
# print('%.0f'%hF + ' hora(s)')
# print('%.0f'%mF + ' minuto(s)')
# print('%.0f'%sF + ' segundo(s)')
# =============================================================================


# =============================================================================
# #1064
# i = 0
# u = 0
# media = 0
# lst = []
# while i < 6:
#     a = float(input())
#     lst.append(a)
#     i += 1
# for x in lst:
#     if x > 0:
#         u +=1
#         media += x
# print(str(u) + " valores positivos")
# media = media/u
# print("%.1f" %media)
# =============================================================================

# =============================================================================
# #1065
# i = 0
# u = 0
# lst = []
# while i < 5:
#     a = float(input())
#     lst.append(a)
#     i += 1
# for x in lst:
#     if x%2 == 0:
#         u +=1
# print(str(u) + " valores pares")
# =============================================================================

# =============================================================================
# #1066
# 
# i = 0
# par = 0
# impar = 0
# pos = 0
# neg = 0
# lst = []
# while i < 5:
#     a = int(input())
#     lst.append(a)
#     i += 1
# for x in lst:
#     if x%2 == 0: par +=1
#     if x%2 != 0: impar +=1
#     if x>0: pos +=1
#     if x<0: neg +=1
#         
# print(str(par) + " valor(es) par(es)")
# print(str(impar) + " valor(es) impar(es)")
# print(str(pos) + " valor(es) positivo(s)")
# print(str(neg) + " valor(es) negativo(s)")
# =============================================================================

# =============================================================================
# #1067
# num_odd = [print(num) for num in range(int(input())+1) if num % 2 != 0]
#===========================================================================

# =============================================================================
# #1070
# num_in = int(input())
# num_odd = [print(num) for num in range(num_in,num_in+12) if num % 2 != 0]
# =============================================================================


# =============================================================================
# #1071
# a = int(input())
# b = int(input())
# y = 0
# if a < b: num_odd = [num for num in range(a+1,b) if num % 2 != 0]
# else : num_odd = [num for num in range(b+1,a) if num % 2 != 0]
# for x in num_odd: 
#     y = y + x 
# 
# print(y)
# =============================================================================

# =============================================================================
# #1072
# i = int(input())
# u = 0
# lst = []
# while u < i:
#     a = int(input())
#     lst.append(a)
#     u += 1
# 
# numIn = 0
# numOut = 0
# 
# for x in lst:
#     if x in range(10,21): numIn += 1
#     else: numOut += 1
#     
# print(str(numIn)+ " in")
# print(str(numOut)+ " out")
# =============================================================================
        
# =============================================================================
# #1073
# 
# num_odd = [num for num in range(1,int(input())+1) if num % 2 == 0]
# 
# for x in num_odd: print(str(x) +"^2 = " + str(x**2))
# =============================================================================

# =============================================================================
# #1074
# 
# i = int(input())
# u = 0
# lst = []
# while u < i:
#     a = int(input())
#     lst.append(a)
#     u += 1
# 
# for x in lst:
#     text = ""
#     if x%2 == 0: text = text + "EVEN "
#     if x%2 != 0: text = text + "ODD "
#     if x > 0: text = text + "POSITIVE"
#     if x < 0: text = text + "NEGATIVE"
#     if x == 0: text = "NULL"
#     print(text)
# =============================================================================

# =============================================================================
# #1075
# a = int(input())
# num_odd = [print(num) for num in range(1,10000) if num % a == 2]
# =============================================================================

# =============================================================================
# #1078
# a = int(input())
# lst = [num for num in range(1,11)]
# 
# for x in lst: print("{0} x {1} = {2}".format(x, a, x*a))
# =============================================================================

# =============================================================================
# #1079
# i = int(input())
# u = 0
# lst = []
# while u < i:
#     a, b, c = map(float,input().split())
#     a = a*2
#     b = b*3
#     c = c*5
#     media = (a+b+c)/10
#     lst.append(media)
#     u +=1    
# for x in lst: print("%.1f"%x)
# =============================================================================

# =============================================================================
# #1080
# 
# u = 0
# lst = []
# x1 = 0
# x2 = 0
# while u < 100:
#     a = int(input())
#     lst.append(a)
#     u +=1    
# for x in lst:
#     if x > x1:
#         x1 = x
#         x2 = lst.index(x)
# print("{0}\n{1}".format(x1,x2+1))
# =============================================================================

# =============================================================================
# #1094
# 
# qntTest = int(input())
# listaCobaia = []
# i = 0
# totalCobaia = 0
# totalCoelho = 0
# totalRato = 0
# totalSapo = 0
# while i < qntTest:
#     numCobaia, tipoCom = input().split()
#     i +=1
#     numCobaia = int(numCobaia)
#     listaCobaia.append((numCobaia,tipoCom))
# 
# for x in listaCobaia:
#     totalCobaia += x[0]
#     if x[1] == "C": totalCoelho += x[0]
#     if x[1] == "R": totalRato += x[0]
#     if x[1] == "S": totalSapo += x[0]
# print("Total: "+ str(totalCobaia )+ " cobaias")
# print("Total de coelhos: "+ str(totalCoelho))
# print("Total de ratos: "+ str(totalRato))
# print("Total de sapos: "+ str(totalSapo))
# 
# print("Percentual de coelhos: %.2f" %((totalCoelho/totalCobaia)*100) + " %")
# print("Percentual de ratos: %.2f" %((totalRato/totalCobaia)*100) + " %")
# print("Percentual de sapos: %.2f" %((totalSapo/totalCobaia)*100) + " %")
# =============================================================================

# =============================================================================
# #1095
# j = 60
# i = 1
# while j >= 0:
#     print("I={0} J={1}".format(i,j))
#     i += 3
#     j -= 5
# =============================================================================

# =============================================================================
# #1096
# 
# i = 1
# j = 7
# 
# while i <= 9:
#     while j > 5:
#         print("I={0} J={1}".format(i,j))
#         j -= 1
#     print("I={0} J={1}".format(i,j))
#     i += 2
#     j += 2
# =============================================================================

# =============================================================================
# #1097
# 
# i = 1
# j = 7
# z = 5
# while i <= 9:
#     while j > z:
#         print("I={0} J={1}".format(i,j))
#         j -= 1
#     print("I={0} J={1}".format(i,j))
#     i += 2
#     j += 4
#     z += 2
# =============================================================================

# =============================================================================
# #1098
# 
# i = 0
# j = 1
# z = 3
# lst = []
# while i < 2:
#     contador = 0
#     while contador <= 2:
#         if round(i,1) == 1.0:
#             i = int(i)
#             j = int(j)
#             print("I={0} J={1}".format(i,j))
#         elif i >= 1.9: 
#             i = int(2)
#             j = int(j)
#             print("I={0} J={1}".format(i,j))
#         else:
#             print("I={0} J={1}".format(round(i,1),round(j,1)))
#         j += 1
#         contador += 1
#     i += 0.2
#     j -= 2.8
#     z += 0.2
# =============================================================================

# =============================================================================
# #1099
# casoTest = int(input())
# iterator = 0
# iteratorFor = 0
# while iterator < casoTest:
#     somaImpar = 0
#     rangeA, rangeB = map(int,input().split())
#     if rangeA > rangeB: num_odd = [num for num in range(rangeB+1,rangeA) if num%2 != 0]
#     else: num_odd = [num for num in range(rangeA+1,rangeB) if num%2 != 0]
#     for iteratorFor in num_odd:
#         somaImpar += iteratorFor
#     print(somaImpar)
#     iterator += 1
# =============================================================================
        
# =============================================================================
# #1101
# rangeA, rangeB = map(int,input().split())
# while rangeA > 0 and rangeB > 0:
#     somaGeral = 0
#     finalPrint = ""
#     if rangeA > rangeB: num_odd = [num for num in range(rangeB,rangeA+1)]
#     else: num_odd = [num for num in range(rangeA,rangeB+1)]
#     for iteratorFor in num_odd:
#         somaGeral += iteratorFor
#         finalPrint += str(iteratorFor) + " "
#     print(str(finalPrint) + "Sum=" +str(somaGeral))
#     rangeA, rangeB = map(int,input().split())
# =============================================================================

# =============================================================================
# #1113
# while True:
#     num1, num2 = map(int,input().split())
#     if num1 > num2: print("Decrescente")
#     elif num2 > num1: print("Crescente")
#     elif num1 == num2: break
# =============================================================================

# =============================================================================
# #1114
# 
# while True:
#     senha = int(input())
#     if senha == 2002:
#         print("Acesso Permitido")
#         break
#     elif senha != 2002: print("Senha Invalida")
# =============================================================================

# =============================================================================
# #1115
# while True:
#     x, y = map(float,input().split())
# 
#     ponto_list = ["primeiro", "segundo", "terceiro", "quarto"]
# 
#     if (x > 0 and y > 0): print(ponto_list[0])
#     elif (x < 0 and y > 0): print(ponto_list[1])
#     elif (x < 0and y < 0): print(ponto_list[2])
#     elif (x > 0 and y < 0): print(ponto_list[3])
#     elif (x == 0 or y == 0): break
# =============================================================================

# =============================================================================
# #1116
# 
# cases = int(input())
# 
# for i in range(cases):
#     num1, num2 = map(int,input().split())
#     if num2 == 0:
#         print("divisao impossivel")
#     else:
#         print(num1/num2)
# =============================================================================

# =============================================================================
# #1117
# media = None
# notaList = []
# while media == None:
#     nota = float(input())
#     if nota >= 0 and nota <= 10:
#         notaList.append(nota)
#         if len(notaList) == 2:
#             media = (notaList[0]+notaList[1])/2
#             print("media = %.2f" %media)
#     else:
#         print("nota invalida")
# =============================================================================
    
#1118

media = None
notaList = []
iterator = 0
while iterator < 3:
    if iterator == 2:
        resposta = int(input("novo calculo (1-sim 2-nao)"))
        if resposta == 1:       
            iterator -= 1
            nota = float(input())
            if nota >= 0 and nota <= 10:
                iterator += 1
                notaList.append(nota)
                if len(notaList) == 2:
                    media = (notaList[0]+notaList[1])/2
                    print("media = %.2f" %media)
            else:
                print("nota invalida")
                break
    if nota >= 0 and nota <= 10:
        iterator += 1
        notaList.append(nota)
        if len(notaList) == 2:
            media = (notaList[0]+notaList[1])/2
            print("media = %.2f" %media)
    else:
        print("nota invalida")










































               