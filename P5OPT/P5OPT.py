import pandas as pd
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import csv
#Note: Copy and Paste this whole code into your document

#Auxiliar Functions
def isnan(str):
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
#Detects if a string includes a number
def equals(a,b):
    if a == b:
        return True
    else:
        return False
#Detects if two inputs are equal (any type)
def dig(n):
    dig = list()
    for i in str(n):
        if i.isnumeric() == False:
            continue
        else:
            dig.append(int(i))
    return dig
#Number of digits of a numerical string
def exception(x):
    a = dig(x)
    b = a[:]
    a.pop(-1)
    tail = b[-1]
    return all(list(map(lambda x: equals(x,0), a))) and (equals(tail,1) or equals(tail,2))
#Detects exception for code print_error mapping is based on
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
#Detects the position among the digits of the numerical string in which truncation begins
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
#Truncates y from the nth digit on

#Relevant Functions to Use
def plot(xs,str,g): #It tells apart between single tables of data and several of them
    tipos_curva = ['Lineal','Cuadrática','Cúbica']
    if type(xs) is dict:
        vars = list(xs.keys())
    else:
        vars = list(xs[0].keys())
    if isnan(str):
        reg = np.polyfit(xs[vars[0]][0], xs[vars[1]][0], deg=g, full=False, cov=True)
        corr_matrix = np.corrcoef(xs[vars[0]][0], xs[vars[1]][0])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], xs[vars[0]][0])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot(xs[vars[0]][0], trend, 'r',
                label=f'{vars[1]}= %.5f $\cdot$ {vars[0]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter(xs[vars[0]][0], xs[vars[1]][0], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[0]} {xs[vars[0]][2][0]}', ylabel=f'{vars[1]} {xs[vars[1]][2][0]}',
               title=f'Dependencia {tipos_curva[g-1]} ({vars[0]}, {vars[1]}).')
        ax.legend(loc='best')
        fig.savefig(f'{str}.pdf')
        plt.show()
        errs_coefs = list()
        for i in range(0,g+1):
            errs_coefs.append((reg[1])[i,i])
        dicto = {"Coeffs": reg[0], "Errs":errs_coefs, "Rsq": R_sq}
    else:
        n = int(str[-1])
        reg = np.polyfit((xs[n])[vars[0]][0], (xs[n])[vars[1]][0], deg=g, full=False, cov=True)
        corr_matrix = np.corrcoef((xs[n])[vars[0]][0], (xs[n])[vars[1]][0])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], (xs[n])[vars[0]][0])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot((xs[n])[vars[0]][0], trend, 'r',
                label=f'{vars[1]}= %.5f $\cdot$ {vars[0]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter((xs[n])[vars[0]][0], (xs[n])[vars[1]][0], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[0]} {xs[vars[0]][2][0]}', ylabel=f'{vars[1]} {xs[vars[1]][2][0]}',
               title=f'Dependencia {tipos_curva[g-1]} ({vars[0]}, {vars[1]}). Paquete de medidas {n + 1}')
        ax.legend(loc='best')
        fig.savefig(f'Figura{n}.pdf')
        plt.show()
        errs_coefs = list()
        for i in range(0, g + 1):
            errs_coefs.append((reg[1])[i, i])
        dicto = {"Coeffs": reg[0], "Errs": errs_coefs, "Rsq": R_sq}
    return dicto
#Given either a dictionary or array of dictionaries adequating to the shape
#{"x axis variable":[[values],[erros],['(measure units)']], "y axis variables":[analog]},
#a str indicating the desired name for the plot (in case ur plot is based on a single
#data set/dictionary, enter a name with no numbers. Otherwise, type something
#, but ensure to type as the last cell of that name the ordinal to which that data set
#corresponds) and the degree g of the desired plotted polynomial (up to 3rd degree),
#it returns a dictionary with the coefficients, its errors and R^2. It also saves your
#plot inside the working directory
def compute_errors(expr,dict):
    listsymbs = ''
    for i in dict.keys():
        listsymbs += f'{i} '
    errors = list()
    simbolos = symbols(listsymbs)[:]
    vartuple = (simbolos[0],)
    for j in range(1,len(simbolos)):
        vartuple += (simbolos[j],)
    valtuple = list()
    firstname = list(dict.keys())[0]
    names = list(dict.keys())
    names.pop(0)
    for j in range(0, len((dict[firstname])[0])):
        valtuple.append((((dict[firstname])[0])[j],))
        for l in names:
            valtuple[j] += (((dict[l])[0])[j],)
    for j in range(0,len((dict[firstname])[0])):
        errors.append(0)
        for i, k in enumerate(list(dict.keys())):
            f = lambdify([vartuple], Derivative(expr, simbolos[i]).doit())
            errors[j] += float(abs(f(valtuple[j]))) * ((dict[k])[1])[j]
    return errors
#Advice: firstly, save the set of variables featuring in the expression
#u'll use as follows:
#var1, var2, ... = symbols('var1 var2 ... ')
#Then, given a similar directory shape as the one used for plot
#< Note that the names of the vars must coincide with the
#names of the vars within the dictionary >
#and an expression Expr(vars) (no equality, just right term) relating the variables
#of the dictionary, it returns an array featuring the errors of each y(vars) = Expr(vars)
def print_error(x,y):
    if x == 0 and y == 0:
        return f'0 \u00B1 0'
    elif x != 0 and y == 0:
        return f'{x} \u00B1 0'
    elif x == 0 and y != 0:
        return f'0 \u00B1 {y}'
    else:
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
#Prints x +- y already truncated
def csvfile(dict,str):
    vars = list(dict.keys())
    vartuple = (vars[0],)
    vars.pop(0)
    for i in vars:
        vartuple += (i,)
    if isnan(str):
        with open(f'table {vartuple}.csv', 'w+', newline='') as f:  # You will need 'wb' mode in Python 2.x
            w = csv.DictWriter(f, dict.keys())

            for i in range(0, len(dict[list(dict.keys())[0]][0])):
                line = {}
                for j in list(dict.keys()):
                    line[j] = print_error((dict[j])[0][i],(dict[j])[1][i])
                w.writerow(line)
    else:
        n = int(str[-1])
        with open(f'table {vartuple} {n}.csv', 'w+', newline='') as f:  # You will need 'wb' mode in Python 2.x
            w = csv.DictWriter(f, dict.keys())

            for i in range(0, len(dict[list(dict.keys())[0]][0])):
                line = {}
                for j in list(dict.keys()):
                    line[j] = print_error((dict[j])[0][i],(dict[j])[1][i])
                w.writerow(line)
#Saves a csvfile (so that later u can import it to the "Create LaTeX Tables" online tool)
#resembling a table filled with x +- errx already truncated. Similar structure of the
#dictionary

##Ley de Malus
theta = symbols('theta')
errsV = list()
for _ in range(0,10):
    errsV.append(0.1)
errstheta = list()
for _ in range(0,10):
    errstheta.append(float(pi/180))
angles = {'theta':[list(np.linspace(float(pi/2),0,10)),errstheta], 'V':[[0.5,1.6,4.6,9.4,14.8,20.3,25.9,30.8,33.1,34.2],errsV]}
errscos = compute_errors((cos(theta))**2,angles)
errscos[0] = 0
costheta = list()
for i in angles['theta'][0]:
    costheta.append(float((cos(i)))**2)
costheta[0] = 0
dom = {'cos²(θ)':[costheta,errscos, ['']], 'V':[[0.5,1.6,4.6,9.4,14.8,20.3,25.9,30.8,33.1,34.2],errsV,['(mV)']]}
reg1 = plot(dom,'DepLincosV', 1)
regdict = {'theta':[list(np.linspace(90,0,10)),list(map( lambda x : int(x),np.ones(10)))]}
regdict.update(dom)
csvfile(regdict,'dom')
##Sacarimetría
vols = list()
vols.append(90)
for i in range(0,7):
    vols.append(vols[i] + 30)
gssugar = 0.3*90
concs = list()
for i in vols:
    concs.append(gssugar/i)

errc = list()
for _ in range(0,8):
    errc.append(0.08)
errdeltheta = list()
for _ in range(0,8):
    errdeltheta.append(2)
varangles = {'c':[concs,errc,['(g/cm³)']], 'Δθ':[list(map(lambda x: x-253,[213,223,227,231,236,238,240,241])),errdeltheta,['(º)']]}
reg2 = plot(varangles,'DepLinvarangles',1)
csvfile(varangles,'varangles')