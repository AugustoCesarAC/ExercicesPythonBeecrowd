# -*- coding: utf-8 -*-
"""
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.



Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".



@author: AC
"""

#1051         
    
a = float(input())

new = 0
new2 = 0
joker = 0

if a <= 2000:
    print("Isento")
elif a > 2000 and a <= 3000:
    a = (a-2000)*0.08
    print("R$ %.2f"%(a))
elif a > 3000 and a <= 4500:
    new = (a - 3000)*0.18
    a = 1000 * 0.08
    print("R$ %.2f"%(a + new))
elif a > 4500:
    while a > 4500:
        a = a - 1 
        joker = joker + 1
    joker = joker*0.28
    new = (a - 3000.01)*0.18
    a = 1000 * 0.08
    print("R$ %.2f"%(joker + new + a))