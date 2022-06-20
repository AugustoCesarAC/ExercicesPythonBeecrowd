# -*- coding: utf-8 -*-
"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

@author: AC
"""

N = int(input())
NewN = N
N100 = 0
N50 = 0
N20 = 0
N10 = 0
N5 = 0
N2 = 0
N1 = 0        
if (N > 0) and (N < 1000000):



    while N >= 100:
        N100 = N100 + 1
        N = N - 100
                
    while N >= 50:
        N50 = N50 + 1
        N = N - 50
                
    while N >= 20:
        N20 = N20 + 1
        N = N - 20
                
    
    while N >= 10:
        N10 = N10 + 1
        N = N - 10
            
    while N >= 5:
        N5 = N5 + 1
        N = N - 5
                
    while N >= 2:
        N2 = N2 + 1
        N = N - 2
                
    while N >= 1:
        N1 = N1 + 1
        N = N - 1
                
    print(NewN)
    print(str(N100) + " nota(s) de R$ 100,00")
    print(str(N50) + " nota(s) de R$ 50,00")
    print(str(N20) + " nota(s) de R$ 20,00")
    print(str(N10) + " nota(s) de R$ 10,00")
    print(str(N5) + " nota(s) de R$ 5,00")
    print(str(N2) + " nota(s) de R$ 2,00")
    print(str(N1) + " nota(s) de R$ 1,00")
else: 
    print("Caquitou")