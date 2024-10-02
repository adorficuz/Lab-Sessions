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
C = list()

for i in range(25,125,5):
    T.append(i)

for i in range(121,136):
    T.append(i)

for i in range(136,155,5):
    T.append(i)


T1 = list()
C1 = list()

epsr = list()
epsr1 = list()
for i,j in C,C1:
    epsr.append(i/Co)
    epsr1.append(j/Co1)

errsT = list()
errsT1 = list()
for i,j in T,T1:
    errsT.append(1E-2)
    errsT1.append(1E-2)
errC = 0
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

paraT = list()
paraT1 = list()

for i in T:
    if i < Tc:
        pass
    else:
        paraT.append(i)
for i in T1:
    if i < Tc1:
        pass
    else:
        paraT1.append(i)

InvDelT = list()
InvDelT1 = list()

for i,j in T,T1:
    o = (i-Tc)**(-1)
    o1 = (j-Tc1)**(-1)
    InvDelT.append(o)
    InvDelT1.append(o1)

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


part2dicti = {'(T-Tc)^-1':[InvDelT,list(map(lambda x: 2*x, errsT)),'(ºC^-1)'],'Χe':[list(map(lambda x: x-1, paraepsr)),errsepsr,['(F/m)']]}
part2dicti1 = {'(T-Tc)^-1':[InvDelT1,list(map(lambda x: 2*x, errsT1)),'(ºC^-1)'],'Χe':[list(map(lambda x: x-1, paraepsr1)),errsepsr1,['(F/m)']]}

reg = plot(part2dicti,'DepLindicti',1)
csvfile(dicti,'dicti')

reg1 = plot(part2dicti1,'DepLindicti1',1)
csvfile(dicti1,'dicti1')