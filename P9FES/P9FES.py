import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit
from Regression_Functions import *
#Note: Copy and Paste this whole code into your document
lb = -2
ub = 3
epso = 8.85E-12
r = 4.28E-3
errr = 1E-5
A = np.pi * r**2
errA = np.pi * 2 * errr * r
d = 1.86E-3
errd = 1E-5
A1 = (10E-3)*(6E-3)
errA1 = sqrt(((5E-4)*(10E-3))**2 + ((5E-4)*(6E-3))**2)
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

epsrdicto = list()
for i in C:
    epsrdicto.append(i/Co)
dictio = {'T':[Ttot,[1],['(ºC)']], 'epsr':[epsrdicto,[1],['']]}
varso = list(dictio.keys())
figo, axo = plt.subplots()
plt.ticklabel_format(axis='both',style='sci',scilimits=(-2,3))
axo.set_axisbelow(True)
axo.grid(color='gray', linestyle='-.', linewidth=0.5)
axo.scatter((dictio[varso[0]][0])[0:len(T)], (dictio[varso[1]][0])[0:len(T)], label='Puntos Ida')
axo.scatter((dictio[varso[0]][0])[len(T):len(T)+len(Tpri)], (dictio[varso[1]][0])[len(T):len(T)+len(Tpri)], label='Puntos Vuelta')
axo.set(xlabel=f'{varso[0]} {dictio[varso[0]][2][0]}', ylabel=f'{varso[1]} {dictio[varso[1]][2][0]}',
               title=f'Dependencia ({varso[0]}, {varso[1]}) para BaTiO3.')
axo.legend(loc='best')
figo.savefig('Graf0.pdf')
plt.show()
Cmean = list()
for i in range(0,8):
    Cmean.append(C[i])
for i in range(0,len(Tpri)):
    Cmean.append((C[8+i]+C[-1-i])/2)
T1 = list()
for i in range(480,601,1):
    if i == 523:
        pass
    else:
        T1.append(i)
T1.reverse()
T1 = list(map(lambda x: x/10, T1))
C1 = [146,143,141,140,139,139,139,140,140,141,141,142,143,144,145,146,147,148,150,151,152,154,155,157,159,160,162,164,166,168,170,173,175,178,180,183,186,189,193,195,198,202,206,210,215,218,223,227,232,237,241,248,254,260,268,276,284,293,301,312,323,332,346,357,375,390,407,429,449,478,508,535,570,614,658,735,812,869,904,1045,1207,1432,1909,2381,3349,4049,4009,3334,2482,2158,2064,1785,1583,1450,1314,1284,1138,1046,990,934,884,841,793,760,730,696,664,646,618,601,574,556,538,522,508,492,477,463,452,440]
C1 = list(map(lambda x : x* 10**(-12), C1))
epsr = list()
epsr1 = list()
for i in Cmean:
    epsr.append(i/Co)

for i in C1:
    epsr1.append(i/Co1)

errsT = [0.1]
errsT1 = [0.1]
errC = 1E-12
errsepsr = list()
for i in Cmean:
    o = sqrt(((errC)/(Co))**2 + ((i * errCo)/(Co**2))**2)
    errsepsr.append(o)

errsepsr1 = list()
for i in C1:
    o = sqrt(((errC)/(Co1))**2 + ((i * errCo1)/(Co1**2))**2)
    errsepsr1.append(o)

Cmean = list(map(lambda x: x * 1E12, Cmean))
errsCmean = [1]

for i in range(0,len(T)):
    T[i] = float(T[i])

for i in range(0,len(T1)):
    T1[i] = float(T1[i])
firstdict = {'T':[T,errsT,['(ºC)']],'C':[Cmean,errsCmean,['(pF)']],'εr':[epsr,errsepsr,['']]}
csvfile(firstdict,'firstdict',lb,ub)
C1 = list(map(lambda x: x*1E12, C1))
errsC1 = [1]
firstdict1 = {'T':[T1,errsT1,['(ºC)']],'C':[C1,errsC1,['(pF)']],'εr':[epsr1,errsepsr1,['']]}
csvfile(firstdict1,'firstdictone',lb,ub)
dicti = {'T':[T,errsT,['(ºC)']],'εr':[epsr,errsepsr,['']]}
dicti1 = {'T':[T1,errsT1,['(ºC)']],'εr':[epsr1,errsepsr1,['']]}
csvfile(dicti,'dicti',lb,ub)
csvfile(dicti1,'dictione',lb,ub)

vars = list(dicti.keys())
fig, ax = plt.subplots()
plt.ticklabel_format(axis='both',style='sci',scilimits=(-2,3))
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
plt.ticklabel_format(axis='both',style='sci',scilimits=(-2,3))
ax1.set_axisbelow(True)
ax1.grid(color='gray', linestyle='-.', linewidth=0.5)
ax1.scatter(dicti1[vars1[0]][0], dicti1[vars1[1]][0], label='Puntos Experimentales')
ax1.set(xlabel=f'{vars1[0]} {dicti1[vars1[0]][2][0]}', ylabel=f'{vars1[1]} {dicti1[vars1[1]][2][0]}',
               title=f'Dependencia ({vars1[0]}, {vars1[1]}) para Sulfato de Triglicina.')
ax1.legend(loc='best')
fig1.savefig('Graf2.pdf')
plt.show()

Tc = 131.9
Tc1 = 51.35
errTc = 0.1
errTc1 = 0.1
paraT = list()
paraT1 = list()
errsparaT = [0.1]
errsparaT1 = [0.1]

for i in range(0,len(T)):
    if T[i] < Tc:
        pass
    else:
        paraT.append(T[i])
for i in range(0,len(T1)):
    if T1[i] < Tc1:
        pass
    else:
        paraT1.append(T1[i])


discard = len(T) - len(paraT)
discard1 = len(T1) - len(paraT1)

paraepsr = list()
paraepsr1 = list()
paraInvXe = list()
paraInvXe1 = list()
errsparaInvXe = list()
errsparaInvXe1 = list()
num = -1
num1 = -1

for i in range(0,len(epsr)):
    num += 1
    if num < discard:
        pass
    else:
        paraepsr.append(epsr[i])
        paraInvXe.append(1/(epsr[i]-1))
        errsparaInvXe.append(errsepsr[i]/((epsr[i]-1)**2))

for i in range(0,len(paraT1)):
    paraepsr1.append(epsr1[i])
    paraInvXe1.append(1 / (epsr1[i] - 1))
    errsparaInvXe1.append(errsepsr1[i] / ((epsr1[i] - 1) ** 2))

parttwodicti = {'T':[paraT, errsparaT, ['(ºC)']], 'Χe^-1':[paraInvXe, errsparaInvXe, ['']]}
parttwodictione = {'T':[paraT1, errsparaT1, ['(ºC)']], 'Χe^-1':[paraInvXe1, errsparaInvXe1, ['']]}


reg = plot(parttwodicti, ['DepLindicti','Titanato de Bario'], 1)

reg1 = plot(parttwodictione, ['DepLindictione','Sulfato de Triglicina'], 1)

for i in range(0,4):
    paraInvXe.pop(0)
    errsparaInvXe.pop(0)
    paraT.pop(0)


for i in range(0,6):
    paraInvXe1.pop(0)
    errsparaInvXe1.pop(0)
    paraT1.pop(0)
for i in range(0,4):
    paraInvXe1.pop(-1)
    errsparaInvXe1.pop(-1)
    paraT1.pop(-1)

parttwodictipri = {'T':[paraT,errsparaT,['(ºC)']],'Χe^-1':[paraInvXe,errsparaInvXe,['(m/F)']]}
regpri = plot(parttwodictipri,['DepLindictipri','Titanato de Bario'],1)

parttwodictiprione = {'T':[paraT1,errsparaT1,['(ºC)']],'Χe^-1':[paraInvXe1,errsparaInvXe1,['(m/F)']]}
regpri1 = plot(parttwodictiprione,['DepLindictiprione','Sulfato de Triglicina'],1)

csvfile(parttwodictipri, 'parttwodictipri',lb,ub)
csvfile(parttwodictiprione, 'parttwodictiprione',lb,ub)

CurCt = (regpri['Coeffs'][0])**(-1)
ErrCurCt = (regpri['Errs'][0]) * (regpri['Coeffs'][0])**(-2)
Tcreg = -(regpri['Coeffs'][1])/(regpri['Coeffs'][0])
ErrTcreg = sqrt(((regpri['Errs'][1])/(regpri['Coeffs'][0]))**2 + ((((regpri['Coeffs'][1])*(regpri['Errs'][0]))/((regpri['Coeffs'][0])**2))**2))
CurCt1 = (regpri1['Coeffs'][0])**(-1)
ErrCurCt1 = (regpri1['Errs'][0]) * (regpri1['Coeffs'][0])**(-2)
Tcreg1 = -(regpri1['Coeffs'][1])/(regpri1['Coeffs'][0])
ErrTcreg1 = sqrt(((regpri1['Errs'][1])/(regpri1['Coeffs'][0]))**2 + ((((regpri1['Coeffs'][1])*(regpri1['Errs'][0]))/((regpri1['Coeffs'][0])**2))**2))