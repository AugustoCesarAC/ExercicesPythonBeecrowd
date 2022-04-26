# =============================================================================
# #1019
# '''
# seg = int(input())  1019
# 
# tempo = ""
# 
# tempo_list = [3600, 60, 1]
# for x in tempo_list:
#     
#     timing = int(seg / x)
#     
#      
#     if x == 1:
#         tempo = tempo + str(timing) 
#     else:
#         tempo = tempo + str(timing) + ":"
# 
#     seg = seg - (x*timing)
# 
# print (tempo)'''
# =============================================================================



# =============================================================================
# #1020
# '''
# tex = ""   1020
# ano = " ano(s)"
# mes = " mes(es)"
# diatex = " dia(s)"
# 
# dia = int(input())
# 
# dia_list = [365, 30, 1]
# for x in dia_list:
#     
#     rest = int( dia / x )
#     
#     if x == 365:
#         tex = str(rest) + ano
#     elif x == 30:
#         tex = str(rest) + mes 
#     else:
#         tex = str(rest) + diatex 
#     
#     dia = dia - (x*rest)
#     
#     print(tex)'''
# =============================================================================


# =============================================================================
# #1021
# '''from decimal import*  1021
# getcontext().prec = 4    
# nota = " nota(s) de R$ "
# moeda = " moeda(s) de R$ "
# dinheiro = Decimal(input())
# 
# coringa = 0
# 
# nota_list = [100, 50, 20, 10, 5, 2]
# moeda_list = list(map(Decimal, [1 ,0.50, 0.25, 0.10, 0.05, 0.01]))
# 
# i = 0
# print("NOTAS:")
# while i < len(nota_list):
#     if i == i:
#         coringa = int(dinheiro/nota_list[i])
#         print(str(coringa) + nota + "%.2f" %nota_list[i])        
#         dinheiro = Decimal(dinheiro - (nota_list[i]*coringa))
#         i = i+1
# 
# im = 0
# coringam = 0
# print("MOEDAS:")
# while im < len(moeda_list):
#     if im == im:
#         coringam = int(dinheiro/moeda_list[im])
#         print(str(coringam) + moeda + "%.2f" %moeda_list[im])
#         dinheiro = Decimal(dinheiro - (moeda_list[im]*coringam))
#         im = im + 1'''
# =============================================================================
        
        
# =============================================================================
# '''
# a, b, c, d = map(int,input().split()) 1035
# #SE B > C e D > A e C + D > A + B 
# #SE C e D > 0
# #SE A % 2
# 
# resto = a%2
# 
# if (b > c and d > a and c+d > a+b and c > 0 and d > 0 and resto == 0 ):
#     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")   ''' 
# =============================================================================
        

        #1036
# =============================================================================
# '''
# a, b, c = map(float, input().split()) 
# 
# deltat = (b**2)-(4*a*c)
# 
# if a == 0 or deltat < 0:
#     print("Impossivel calcular")
# else:
#     delta = deltat**0.5
#     
#     r1 = ((b*-1) + delta) / (2*a)
#     r2 = ((b*-1) - delta) / (2*a)
#     
#     print("R1 = %.5f" %r1)
#     print("R2 = %.5f" %r2)'''
# =============================================================================



























