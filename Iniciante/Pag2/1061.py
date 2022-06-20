# -*- coding: utf-8 -*-
"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.



@author: AC
"""

#1061

dia1 = input().split()
dia1 = int(dia1[1])

h1, m1, s1 = map(int,input().split(":"))
dia2 = input().split()
dia2 = int(dia2[1])
h2, m2, s2 = map(int,input().split(":"))

seg1 = (dia1*86400)+(h1*3600)+(m1*60)+s1
seg2 = (dia2*86400)+(h2*3600)+(m2*60)+s2
seg3 = seg2-seg1

diaF = seg3//86400
hF = seg3//3600
while hF >= 24: hF = int(hF - 24)

mF = seg3//60
while mF >= 60: mF = int(mF - 60)
    
sF = (seg3-(diaF*86400)-(hF*3600)-(mF*60))

print('%.0f'%diaF + ' dia(s)')
print('%.0f'%hF + ' hora(s)')
print('%.0f'%mF + ' minuto(s)')
print('%.0f'%sF + ' segundo(s)')