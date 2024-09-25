import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from Regression_Functions import *
#Note: Copy and Paste this whole code into your document
d = 8.1 * 10**(-2)
alphao = 0
r1 = 0.11 * 10**(-2)
r2 = 0.11 * 10**(-2)
L = 320* 10**(-3)
S1 = np.pi * r1**2
S2 = np.pi * r2**2
muo = 4 * np.pi * 10**(-7)
Bt = 0.234 *10**(-4)
C1 = (4 * np.pi * d**2 * Bt)/(muo * S1 * (1- (d**3 / ((L**2 + d**2 )**1.5))))
C2 = (4 * np.pi * d**2 * Bt)/(muo * S2 * (1- (d**3 / ((L**2 + d**2 )**1.5))))
I = list()
for i in range(1,22):
    I.append(0.2 + (i-1)*((2-0.2)/36))

for i in range(1,9):
    I.append(1.2 + i*0.1)

for i in range(2,42):
    I.append(2 - (i-1)*((2-0)/40))

for i in range(2,42):
    o = 0 - (i - 1) * ((2 - 0) / 40)
    if o <= -0.9:
        if i % 2 == 1:
            I.append(0 - (i - 1) * ((2 - 0) / 40))
        else:
            pass
    else:
        I.append(o)


for i in range(2,42):
    if i % 2 == 1:
        I.append(-2 + (i - 1) * ((2 - 0) / 40))
    else:
        pass

for i in range(2,42):
    o = (i-1)*((2-0)/40)
    if o >= 0.8:
        if o == 1.3:
            pass
        else:
            if i % 2 == 1:
                I.append(o)
            else:
                pass
    else:
        I.append(o)
I[0] = 0.209
n = 190
H1 = list()
for i in I:
    H1.append(n*i)

I2 = list()

for i in range(1,17):
    o = i*0.05
    I2.append(o)

I2[0] = 0.06

for i in range(1,13):
    o = 0.8 + i*0.1
    I2.append(o)

for i in range(1,22):
    o = 2 - i*0.1
    I2.append(o)

for i in range(1,15):
    o = -0.1 - i*0.05
    I2.append(o)

for i in range(1,13):
    o = -0.8 - i*0.1
    I2.append(o)

for i in range(1,21):
    o = -2 + i*0.1
    I2.append(o)

for i in range(1,15):
    o = 0 + i*0.05
    I2.append(o)

for i in range(1,14):
    o = 0.7 + i*0.1
    I2.append(o)

H2 = list()
for i in I2:
    H2.append(n*i)

alpha11 = [4,6,16,22,26,28,29,30,31,32,33,33,34,34,35,35,36,36,36,37,37,38,38,38,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38,38,38,38,38,38,38,37,37,37,37,37,37,37,36,36,36,36,35,35,34,34,33,33,32,31,29,27,24,15,2,-8,-18,-22,-26,-28,-30,-32,-33,-34,-34,-35,-35,-36,-37,-37,-38,-38,-39,-39,-39,-40,-40,-40,-39,-39,-39,-39,-39,-39,-39,-39,-38,-38,-38,-37,-37,-37,-36,-36,-35,-34,-33,-31,-30,-28,-26,-21,-10,3,13,19,24,27,29,31,32,33,34,34,35,36,36,37,38,38,38,39,39,39,39,39]
alpha21 = [3,5,16,22,25,28,29,31,31,32,33,34,34,35,35,35,36,37,37,37,37,38,38,39,39,39,39,39,40,40,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,38,38,38,38,38,38,37,37,37,37,37,36,36,35,35,35,34,34,33,32,32,31,29,27,24,15,2,-9,-19,-23,-26,-29,-31,-32,-34,-34,-35,-35,-36,-37,-37,-39,-39,-39,-40,-40,-40,-40,-41,-41,-41,-41,-41,-41,-40,-40,-40,-40,-40,-39,-39,-39,-39,-38,-38,-37,-36,-35,-34,-32,-31,-29,-27,-22,-10,3,12,19,24,27,29,31,32,32,33,34,35,35,36,37,38,38,38,39,39,39,39,39]


alpha1 = list()
for i in range(0,len(alpha11)):
    alpha1.append((alpha11[i] + alpha21[i])/2)

alpha12 = [3,5,6,7,7,7,8,8,9,9,9,9,9,10,10,10,10,10,10,11,11,11,11,11,12,12,12,12,12,12,12,12,12,11,11,11,11,11,11,10,10,10,10,10,10,9,9,8,7,5,2,-3,-5,-6,-6,-7,-7,-8,-8,-8,-9,-9,-9,-9,-9,-10,-10,-10,-10,-10,-10,-10,-10,-10,-11,-11,-11,-11,-11,-11,-11,-10,-10,-10,-10,-10,-10,-10,-9,-9,-8,-8,-8,-7,-7,-6,-5,-4,2,5,7,8,8,9,9,9,9,9,9,10,10,10,10,10,11,11,11,11,12,12,12,12]
alpha22 = [3,6,7,7,7,7,7,8,8,9,9,9,9,10,10,10,10,10,11,11,11,11,11,11,11,12,12,12,12,12,12,11,11,11,11,11,11,11,11,10,10,10,10,10,10,9,9,8,7,5,2,-4,-4,-7,-7,-7,-7,-8,-9,-9,-9,-9,-9,-10,-10,-10,-10,-10,-10,-10,-10,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-11,-10,-10,-10,-10,-10,-9,-9,-9,-9,-8,-8,-7,-6,-5,-4,2,5,7,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,11,11,12,12]

alpha2 = list()
for i in range(0,len(alpha12)):
    alpha2.append((alpha12[i] + alpha22[i])/2)
M1 = list()
for i in alpha1:
    M1.append(C1*(np.tan(i) - np.tan(alphao)))

M2 = list()
for i in alpha2:
    M2.append(C2*(np.tan(i) - np.tan(alphao)))

xs = {"H":[H1,list(),['(A/m)']], "M":[M1,list(),['(A/m)']]}
vars = list(xs.keys())
fig, ax = plt.subplots()
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='-.', linewidth=0.5)
ax.scatter(xs[vars[0]][0], xs[vars[1]][0], label='Puntos Experimentales')
ax.set(xlabel=f'{vars[0]} {xs[vars[0]][2][0]}', ylabel=f'{vars[1]} {xs[vars[1]][2][0]}',
               title=f'Dependencia ({vars[0]}, {vars[1]}).')
ax.legend(loc='best')
fig.savefig('Graf1.pdf')
plt.show()

xs1 = {"H":[H2,list(),['(A/m)']], "M":[M2,list(),['(A/m)']]}
vars1 = list(xs.keys())
fig1, ax1 = plt.subplots()
ax1.set_axisbelow(True)
ax1.grid(color='gray', linestyle='-.', linewidth=0.5)
ax1.scatter(xs1[vars1[0]][0], xs1[vars1[1]][0], label='Puntos Experimentales')
ax1.set(xlabel=f'{vars1[0]} {xs1[vars1[0]][2][0]}', ylabel=f'{vars1[1]} {xs1[vars1[1]][2][0]}',
               title=f'Dependencia ({vars1[0]}, {vars1[1]}).')
ax1.legend(loc='best')
fig1.savefig('Graf2.pdf')
plt.show()
