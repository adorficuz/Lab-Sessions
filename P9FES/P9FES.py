import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from Regression_Functions import *
#Note: Copy and Paste this whole code into your document
epso = 8.85E-12
r = 4.28E-3
errr = 1E-5
A = np.pi * r**2
errA = np.pi * 2 * errr
d = 1.86E-3
errd = 1E-5
A1 = (10E-3)*(6E-3)
errA1 = (5E-4)**2
d1 = 2E-3
errd1 = 5E-4
Co = epso * (A/d)
errCo = epso * sqrt((errA/d)**2 + ((A*errd)/(d**2))**2)
Co1 = epso * (A1/d1)
errCo1 = epso * sqrt((errA1/d1)**2 + ((A1*errd1)/(d1**2))**2)
T = list()
Tpri = list()
C = [311,342,310,308,306,306,308,308,309,311,314,320,328,336,346,360,379,404,450,463,488,503,527,551,574,589,596,596,592,585,578,569,560,551,506,470,434,410,391,428,465,508,556,602,609,614,617,615,607,593,570,541,513,491,474,460,449,438,430,397,375,359,347,338,331,325,321,317,315,313]

C = list(map(lambda x : x* 10**(-12), C))


for i in range(30,125,5):
    T.append(i)
    Tpri.append(i)

for i in range(121,136):
    T.append(i)
    Tpri.append(i)

for i in range(140,165,5):
    T.append(i)
    Tpri.append(i)

for i in range(0,7):
    Tpri.pop(0)
Tpri.reverse()
Tpri.pop(0)
Ttot = T + Tpri

Cmean = list()
for i in range(0,8):
    Cmean.append(C[i])
for i in range(0,len(T)):
    Cmean.append((C[8+i]+C[-1-i])/2)
T1 = list()
T1pri = list()

for i in range(30,125,5):
    T1.append(i)
    T1pri.append(i)

for i in range(121,136):
    T1.append(i)
    T1pri.append(i)

for i in range(140,155,5):
    T1.append(i)
    T1pri.append(i)

T1pri.reverse()
T1pri.pop(0)
Ttot1 =  T1 + T1pri

C1 = list()

epsr = list()
epsr1 = list()
for i in C:
    epsr.append(i/Co)

for i in C1:
    epsr1.append(i/Co1)

errsT = list()
errsT1 = list()
for i in T:
    errsT.append(1E-1)
for j in T1:
    errsT1.append(1E-1)
errC = 1E-12
errsepsr = list()
for i in C:
    o = sqrt(((errC)/(Co))**2 + ((C[i] * errCo)/(Co**2))**2)
    errsepsr.append(o)

errsepsr1 = list()
for i in C1:
    o = sqrt(((errC)/(Co1))**2 + ((C1[i] * errCo1)/(Co1**2))**2)
    errsepsr.append(o)
dicti = {'T':[T,errsT,['(ºC)']],'εr':[epsr,errsepsr,['(F/m)']]}
dicti1 = {'T':[T,errsT,['(ºC)']],'εr':[epsr,errsepsr,['(F/m)']]}
csvfile(dicti,'dicti')
csvfile(dicti1,'dicti1')

vars = list(dicti.keys())
fig, ax = plt.subplots()
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='-.', linewidth=0.5)
ax.scatter(dicti[vars[0]][0], dicti[vars[1]][0], label='Puntos Experimentales')
ax.set(xlabel=f'{vars[0]} {dicti[vars[0]][2][0]}', ylabel=f'{vars[1]} {dicti[vars[1]][2][0]}',
               title=f'Dependencia ({vars[0]}, {vars[1]}) para BaTiO3.')
ax.legend(loc='best')
fig.savefig('Graf1.pdf')
plt.show()

vars1 = list(dicti1.keys())
fig1, ax1 = plt.subplots()
ax1.set_axisbelow(True)
ax1.grid(color='gray', linestyle='-.', linewidth=0.5)
ax1.scatter(dicti1[vars1[0]][0], dicti1[vars1[1]][0], label='Puntos Experimentales')
ax1.set(xlabel=f'{vars1[0]} {dicti1[vars1[0]][2][0]}', ylabel=f'{vars1[1]} {dicti1[vars1[1]][2][0]}',
               title=f'Dependencia ({vars1[0]}, {vars1[1]}) para BaTiO3.')
ax1.legend(loc='best')
fig1.savefig('Graf1.pdf')
plt.show()

Tc = 0
Tc1 = 0
errTc = 0
errTc1 = 0
paraT = list()
paraT1 = list()
errsparaT = list()
errsparaT1 = list()

for i,j in T,errsT:
    if i < Tc:
        pass
    else:
        paraT.append(i)
        errsparaT.append(j)
for i,j in T1, errsT1:
    if i < Tc1:
        pass
    else:
        paraT1.append(i)
        errsparaT1.append(j)

InvDelT = list()
InvDelT1 = list()

for i in paraT:
    o = (i-Tc)**(-1)
    InvDelT.append(o)

for i in paraT1:
    o = (i-Tc1)**(-1)
    InvDelT1.append(o)

errsInvDelT = list()
errsInvDelT1 = list()

for i,j in paraT, errsparaT:
    o = sqrt((j/((i-Tc)**2))**2 + (errTc/((i-Tc)**2))**2)
    errsInvDelT.append(o)
for i,j in paraT1, errsparaT1:
    o = sqrt((j/((i-Tc1)**2))**2 + (errTc1/((i-Tc1)**2))**2)
    errsInvDelT1.append(o)

discard = len(T) - len(paraT)
discard1 = len(T1) - len(paraT1)

paraepsr = list()
paraepsr1 = list()
errsparaepsr = list()
errsparaepsr1 = list()
num = -1
num1 = -1

for i,j in epsr,errsepsr:
    num += 1
    if num < discard:
        pass
    else:
        paraepsr.append(i)
        errsparaepsr.append(j)

for i,j in epsr1,errsparaepsr1:
    num1 += 1
    if num1 <= discard1:
        pass
    else:
        paraepsr1.append(i)
        errsparaepsr1.append(j)


part2dicti = {'(T-Tc)^-1':[InvDelT,errsInvDelT,'(ºC^-1)'],'Χe':[list(map(lambda x: x-1, paraepsr)),errsepsr,['(F/m)']]}
part2dicti1 = {'(T-Tc)^-1':[InvDelT1,errsInvDelT1,'(ºC^-1)'],'Χe':[list(map(lambda x: x-1, paraepsr1)),errsepsr1,['(F/m)']]}

reg = plot(part2dicti,'DepLindicti',1)
csvfile(dicti,'part2dicti')

reg1 = plot(part2dicti1,'DepLindicti1',1)
csvfile(dicti1,'part2dicti1')