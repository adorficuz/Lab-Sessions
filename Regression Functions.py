import pandas as pd
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
        ax.set(xlabel=f'{vars[1]} (cm)', ylabel=f'{vars[1]} (cm)',
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
def print_error(x,y):
    return f'{x} \u00B1 {y}'

def postrunc(y):
    stry = str(y)
    digitsy = list()
    for i,k in enumerate(stry):
        digitsy.append(k)
    digitsy.reverse()
    digitsy.append('0')
    digitsy.reverse()
    newstry = ''.join(digitsy)
    pos = 0
    for i, k in enumerate(stry):
        if k.isnumeric() == False:
            pos += 1
        elif k.isnumeric() and newstry[i].isnumeric() == False:
            if int(newstry[i - 1]) == 0 and int(k) == 0:
                pos += 1
            elif (int(newstry[i - 1]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i - 1 + 1]) < 5))):
                return (pos+1)
            else:
                return (pos)
        elif k.isnumeric() and newstry[i + 2].isnumeric() == False:
            if int(newstry[i]) == 0 and int(k) == 0:
                pos += 1
            elif (int(newstry[i]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i + 2]) < 5))):
                return (pos+2)
            else:
                return(pos)
        else:
            if int(newstry[i]) == 0 and int(k) == 0:
                pos += 1
            elif (int(newstry[i]) == 0 and (int(k) == 1 or (int(k) == 2 and int(stry[i + 2]) < 5))):
                return (pos+1)
            else:
                return(pos)

print(postrunc(1215670.0427))

def truncate(y,n):
    digitsy = list()
    for i in str(y):
        if i.isnumeric():
            digitsy.append(int(i))
        else:
            digitsy.append(i)
    digitsy.reverse()
    digitsy.append(0)
    digitsy.reverse()
    if str(digitsy[n+2]).isnumeric() == False:
        if digitsy[n+3] >= 5 and digitsy[n+1] < 9:
            digitsy[n+1] += 1
            return ''.join(list(map(str, digitsy)))
        elif digitsy[n+3] >= 5 and digitsy[n+1] == 9:
            digitsy[n] += 1
            digitsy[n+1] = 0
            return ''.join(list(map(str, digitsy)))
        else:
            digitsy[n+1] += 0
            return ''.join(list(map(str, digitsy)))
    elif str(digitsy[n]).isnumeric() == False:
        if digitsy[n+2] >= 5 and digitsy[n+1] < 9:
            digitsy[n+1] += 1
            return ''.join(list(map(str, digitsy)))
        elif digitsy[n+2] >= 5 and digitsy[n+1] == 9:
            digitsy[n-1] += 1
            digitsy[n+1] = 0
            return ''.join(list(map(str, digitsy)))
        else:
            digitsy[n+1] += 0
            return ''.join(list(map(str, digitsy)))
    else:
        if digitsy[n+2] >= 5 and digitsy[n+1] < 9:
            digitsy[n+1] += 1
            return ''.join(list(map(str, digitsy)))
        elif digitsy[n+2] >= 5 and digitsy[n+1] == 9:
            digitsy[n] += 1
            digitsy[n+1] = 0
            return ''.join(list(map(str, digitsy)))
        else:
            digitsy[n+1] += 0
            return ''.join(list(map(str, digitsy)))

print(truncate(1215670.0427,postrunc(1215670.0427)))
def csvfile(n):
    with open(f'table {n}.csv', 'w+', newline='') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, Results.keys())

        for i in range(10*n, 10*(n+1)):
            line = {}
            for j in list(Results.keys()):
                line[j] = (Results[j])[i]
            w.writerow(line)