import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from Regression_Functions import *
#Note: Copy and Paste this whole code into your document
d = 0
alphao = 0
r1 = 0
r2 = 0
L = 0
S1 = np.pi * r1**2
S2 = np.pi * r2**2
muo = 4 * np.pi * 10**(-7)
Bt = 0.234 *10**(-4)
C1 = (4 * np.pi * d**2 * Bt)/(muo * S1 * (1- (d**3 / ((L**2 + d**2 )**1.5))))
C2 = (4 * np.pi * d**2 * Bt)/(muo * S2 * (1- (d**3 / ((L**2 + d**2 )**1.5))))
I = list()
for i in range(1,38):
    I.append(0.2 + (i-1)*((2-0.2)/36))

for i in range(2,42):
    I.append(2 - (i-1)*((2-0)/40))

for i in range(2,42):
    I.append(0 - (i-1)*((2-0)/40))

for i in range(2,42):
    I.append(-2 + (i-1)*((2-0)/40))

n = 190
H = list()
for i in I:
    H.append(n*i)

alpha11 = list()
alpha21 = list()

alpha1 = list()
for i in range(0,len(alpha11)):
    alpha1.append((alpha11[i] + alpha21[i])/2)

alpha12 = list()
alpha22 = list()

alpha2 = list()
for i in range(0,len(alpha12)):
    alpha2.append((alpha12[i] + alpha22[i])/2)
M1 = list()
for i in alpha1:
    M1.append(C1*(np.tan(i) - np.tan(alphao)))

M2 = list()
for i in alpha2:
    M2.append(C2*(np.tan(i) - np.tan(alphao)))

xs = {"H":[H,list(),['(A/m)']], "M":[M1,list(),['(A/m)']]}
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

xs = {"H":[H,list(),['(A/m)']], "M":[M2,list(),['(A/m)']]}
vars = list(xs.keys())
fig, ax = plt.subplots()
ax.set_axisbelow(True)
ax.grid(color='gray', linestyle='-.', linewidth=0.5)
ax.scatter(xs[vars[0]][0], xs[vars[1]][0], label='Puntos Experimentales')
ax.set(xlabel=f'{vars[0]} {xs[vars[0]][2][0]}', ylabel=f'{vars[1]} {xs[vars[1]][2][0]}',
               title=f'Dependencia ({vars[0]}, {vars[1]}).')
ax.legend(loc='best')
fig.savefig('Graf2.pdf')
plt.show()