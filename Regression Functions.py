import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
def array_to_dict(xs,ys): #This function enables us to import data to a dict
    dict = {}
    for i,k in enumerate(ys):
        dict[i] = xs[k]
    return dict
def isnan(str): #Auxiliar for plot
    boollist = list()
    for i in str:
        if i.isnumeric():
            boollist.append(False)
        else:
            boollist.append(True)
    if all(boollist):
        return True
    else:
        return False
def plot(xs,str): #It tells apart between single tables of data and several of them
    if type(xs) is dict:
        vars = list(xs.keys())
    else:
        vars = list(xs[0].keys())
    if isnan(str):
        reg = np.polyfit(xs[vars[0]], xs[vars[1]], deg=1, full=False, cov=True)
        corr_matrix = np.corrcoef(xs[vars[0]], xs[vars[1]])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], xs[vars[0]])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot(xs[vars[0]], trend, 'r',
                label=f'{vars[1]}= %.5f $\cdot$ {vars[0]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter(xs[vars[0]], xs[vars[1]], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[0]} (cm)', ylabel=f'{vars[1]} (cm)',
               title=f'Dependencia Lineal ({vars[0]}, {vars[1]}).')
        ax.legend(loc='best')
        fig.savefig(f'{str}.pdf')
        plt.show()
        dicto = {"Coeffs": reg[0], "Errs": [(reg[1])[0, 0], (reg[1])[1, 1]], "Rsq": R_sq}
    else:
        n = int(str[-1])
        reg = np.polyfit((xs[n])[vars[0]], (xs[n])[vars[1]], deg=1, full=False, cov=True)
        corr_matrix = np.corrcoef((xs[n])[vars[0]], (xs[n])[vars[1]])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], (xs[n])[vars[0]])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot((xs[n])[vars[0]], trend, 'r',
                label=f'{vars[1]}= %.5f $\cdot$ {vars[0]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter((xs[n])[vars[0]], (xs[n])[vars[1]], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[0]} (cm)', ylabel=f'{vars[1]} (cm)',
               title=f'Dependencia Lineal ({vars[0]}, {vars[1]}). Paquete de medidas {n + 1}')
        ax.legend(loc='best')
        fig.savefig(f'Figura{n}.pdf')
        plt.show()
        dicto = {"Coeffs": reg[0], "Errs": [(reg[1])[0, 0], (reg[1])[1, 1]], "Rsq": R_sq}
    return dicto

def equals(a,b):
    if a == b:
        return True
    else:
        return False

def dig(n):
    dig = list()
    for i in str(n):
        if i.isnumeric() == False:
            continue
        else:
            dig.append(int(i))
    return dig
def exception(x):
    a = dig(x)
    b = a[:]
    a.pop(-1)
    tail = b[-1]
    return all(list(map(lambda x: equals(x,0), a))) and (equals(tail,1) or equals(tail,2))
def postrunc(y):
    if exception(y) == 1:
        return len(str(abs(y)))-1
    else:
        stry = str(abs(y))
        digitsy = list()
        for i, k in enumerate(stry):
            digitsy.append(k)
        digitsy.reverse()
        digitsy.append('0')
        digitsy.reverse()
        digitsy.append('0')
        newstry = ''.join(digitsy)
        pos = 0
        for i, k in enumerate(stry):
            if k.isnumeric() == False:
                pos += 1
            elif k.isnumeric() and newstry[i].isnumeric() == False:
                if int(newstry[i - 1]) == 0 and int(k) == 0:
                    pos += 1
                elif (int(newstry[i - 1]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i + 1]) < 5))):
                    return (pos + 1)
                else:
                    return (pos)
            elif k.isnumeric() and newstry[i + 2].isnumeric() == False:
                if int(newstry[i]) == 0 and int(k) == 0:
                    pos += 1
                elif (int(newstry[i]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i + 1]) < 5))):
                    return (pos + 2)
                else:
                    return (pos)
            else:
                if int(newstry[i]) == 0 and int(k) == 0:
                    pos += 1
                elif (int(newstry[i]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i + 1]) < 5))):
                    return (pos + 1)
                else:
                    return (pos)

def truncate(y,n):
    if exception(y) == 1:
        return str(y)
    else:
        sgn = int(y / abs(y))
        digitsy = list()
        for i in str(abs(y)):
            if i.isnumeric():
                digitsy.append(int(i))
            else:
                digitsy.append(i)
        digitsy.reverse()
        digitsy.append(0)
        digitsy.reverse()
        digitsy.append(0)
        digitsy.append(0)
        digitsy.append(0)
        if str(digitsy[n + 2]).isnumeric() == False:
            if digitsy[n + 3] >= 5 and digitsy[n + 1] < 9:
                digitsy[n + 1] += 1
            elif digitsy[n + 3] >= 5 and digitsy[n + 1] == 9:
                digitsy[n] += 1
                digitsy[n + 1] = 0
            else:
                digitsy[n + 1] += 0
        elif str(digitsy[n]).isnumeric() == False:
            if digitsy[n + 2] >= 5 and digitsy[n + 1] < 9:
                digitsy[n + 1] += 1
            elif digitsy[n + 2] >= 5 and digitsy[n + 1] == 9:
                digitsy[n - 1] += 1
                digitsy[n + 1] = 0
            else:
                digitsy[n + 1] += 0
        else:
            if digitsy[n + 2] >= 5 and digitsy[n + 1] < 9:
                digitsy[n + 1] += 1
            elif digitsy[n + 2] >= 5 and digitsy[n + 1] == 9:
                digitsy[n] += 1
                digitsy[n + 1] = 0
            else:
                digitsy[n + 1] += 0
        posnonnum = 0
        for i in str(abs(y)):
            if i.isnumeric():
                posnonnum += 1
            else:
                break
        if n < posnonnum:
            for i in list(range(n + 2, posnonnum + 1)):
                digitsy[i] = 0
            newdigitsy = list()
            for i in range(1, posnonnum + 1):
                newdigitsy.append(digitsy[i])
        else:
            newdigitsy = list()
            for i in range(1, n + 2):
                newdigitsy.append(digitsy[i])
        newdigitsy[0] *= sgn
        return ''.join(list(map(str, newdigitsy)))

def compute_errors(expr,dict):
    listsymbs = ''
    for i in dict.keys():
        listsymbs += f'{i} '
    errors = list()
    simbolos = symbols(listsymbs)[:]
    vartuple = (symbols(listsymbs)[0],)
    symbols(listsymbs).pop(0)
    for j in symbols(listsymbs):
        vartuple += (j,)
    valtuple = list()
    firstname = list(dict.keys())[0]
    names = list(dict.keys())
    names.pop(0)
    for j in range(0, len((dict[firstname])[0])):
        valtuple.append(((dict[firstname])[j],))
        for l in names:
            valtuple[j] += ((dict[l])[j],)
    for i, k in enumerate(list(dict.keys())):
        errors.append(0)
        f = lambdify([vartuple], Derivative(expr, symbols(listsymbs)[i]))
        errors[i] += abs(f(valtuple)) * (dict[k])[2]
    return errors


def print_error(x,y):
    posnonnum = 0
    for i in str(abs(y)):
        if i.isnumeric():
            posnonnum += 1
        else:
            break
    posnonnum2 = 0
    for i in str(abs(x)):
        if i.isnumeric():
            posnonnum2 += 1
        else:
            break
    if (postrunc(y) - posnonnum) + posnonnum2 < 0:
        return f'{0} \u00B1 {truncate(y, postrunc(y))}'
    else:
        return f'{truncate(x, posnonnum2 + (postrunc(y) - posnonnum))} \u00B1 {truncate(y, postrunc(y))}'

def csvfile(n):
    with open(f'table {n}.csv', 'w+', newline='') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, Results.keys())

        for i in range(10*n, 10*(n+1)):
            line = {}
            for j in list(Results.keys()):
                line[j] = (Results[j])[i]
            w.writerow(line)