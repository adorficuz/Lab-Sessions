import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
#errores
piezadist = 20.0
#1.-Laser-Lente
poslaser = 26.7
poslente = 56.0
e_las_len = piezadist - (poslente - poslaser)
#2.-Lente-Pantalla
newposlente = 277.7
pospant = 291.7
e_len_pant = piezadist - (pospant - newposlente)
#3.-Biprisma-Pantalla
posbip = 43.3
newpospant = 56.6
e_bip_pant = piezadist - (newpospant-posbip)
#4.-Imagen Puntual
poslentepuntual = 51.3
sopri = (pospant - poslentepuntual) + e_len_pant
fpri = 15
def preim_gauss(spri,fpri):
    return [1/((1/spri)-(1/fpri)), 0.6*(abs((fpri**2 - 2*fpri*spri)/((fpri-spri)**2))) , abs(spri*((1/spri)-(1/fpri))), 0.6/fpri]

L = preim_gauss(sopri,fpri)[0] + sopri
e_L = preim_gauss(sopri,fpri)[1] + 0.6
betao = preim_gauss(sopri,fpri)[2]
e_betao = preim_gauss(sopri,fpri)[3]

#5.- Grueso de la práctica
sopri2 = pospant- 58.2 + e_len_pant
#1st Set
spriset = [sopri2]
for i in range(0,9):
    spriset.append(pospant - (110.5 + i*5) + e_len_pant)
betas = list(map(lambda x: preim_gauss(x,fpri)[2], spriset))
e_betas = list(map(lambda x: preim_gauss(x,fpri)[3], spriset))
test1 = [1.525, 3.125/9]
delxpri1 = [3.080,3.220,3.305,3.430,3.580,3.650,3.835,3.900]
for i,k in enumerate(delxpri1):
    delxpri1[i] = k/8
hpriset1 = test1 + delxpri1
data1 = list(map(lambda n: preim_gauss(spriset[n],fpri) + [hpriset1[n]/betas[n]] + [(e_betas[n]*hpriset1[n] + 0.005*betas[n])/(betas[n]**2)] + [L - (spriset[n] + preim_gauss(spriset[n],fpri)[0])] + [e_L + 0.6 + preim_gauss(spriset[n],fpri)[1]],list(range(0,10))))
(data1[0])[-2] = L - (pospant- 48.9 + e_bip_pant)
#2nd Set
test2 = [1.235, 4.020/9]
delxpri2 = [3.655,3.940,4.185,4.250,4.425,4.525,4.630,4.670]
for i,k in enumerate(delxpri2):
    delxpri2[i] = k/8
hpriset2 = test2 + delxpri2
data2 = list(map(lambda n: preim_gauss(spriset[n],fpri) + [hpriset2[n]/betas[n]] + [(e_betas[n]*hpriset2[n] + 0.005*betas[n])/(betas[n]**2)] + [L - (spriset[n] + preim_gauss(spriset[n],fpri)[0])] + [e_L + 0.6 + preim_gauss(spriset[n],fpri)[1]],list(range(0,10))))
(data2[0])[-2] = L - (pospant- 47.9 + e_bip_pant)
#3rd Set
test3 = [0.900]
delxpri3 = [4.280,4.425,4.560,4.640,4.740,4.915,5.085,5.235,5.430]
for i,k in enumerate(delxpri3):
    delxpri3[i] = k/7
hpriset3 = test3 + delxpri3
data3 = list(map(lambda n: preim_gauss(spriset[n],fpri) + [hpriset3[n]/betas[n]] + [(e_betas[n]*hpriset3[n] + 0.005*betas[n])/(betas[n]**2)] + [L - (spriset[n] + preim_gauss(spriset[n],fpri)[0])] + [e_L + 0.6 + preim_gauss(spriset[n],fpri)[1]],list(range(0,10))))
(data3[0])[-2] = L - (pospant- 46.9 + e_bip_pant)
#4th Set
test4 = [0.670]
delxpri4 = [3.840,4.075,4.260,4.505,4.675,4.840,4.965,5.060,5.160]
for i,k in enumerate(delxpri4):
    delxpri4[i] = k/5
hpriset4 = test4 + delxpri4
data4 = list(map(lambda n: preim_gauss(spriset[n],fpri) + [hpriset4[n]/betas[n]] + [(e_betas[n]*hpriset4[n] + 0.005*betas[n])/(betas[n]**2)] + [L - (spriset[n] + preim_gauss(spriset[n],fpri)[0])] + [e_L + 0.6 + preim_gauss(spriset[n],fpri)[1]],list(range(0,10))))
(data4[0])[-2] = L - (pospant- 45.9 + e_bip_pant)
datas = [data1,data2,data3,data4]
#Representaciones
def delxnD(xs,n):
    ys = xs[:]
    for _ in range(0,n+1):
        ys.pop(0)
    delx = list()
    D = list()
    for i in ys:
        delx.append(i[4])
        D.append(i[6])
    return {"$\Delta x$":delx,"D":D}
dom1 = delxnD(data1,0)
dom2 = delxnD(data2,0)
dom3 = delxnD(data3,0)
dom4 = delxnD(data4,0)
doms = [dom1,dom2,dom3,dom4]
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
def plot(xs,str):
    if type(xs) is dict:
        vars = list(xs.keys())
    else:
        vars = list(xs[0].keys())
    if isnan(str):
        reg = np.polyfit(xs[vars[1]], xs[vars[0]], deg=1, full=False, cov=True)
        corr_matrix = np.corrcoef(xs[vars[1]], xs[vars[0]])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], xs[vars[1]])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot(xs[vars[1]], trend, 'r',
                label=f'{vars[0]}= %.5f $\cdot$ {vars[1]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter(xs[vars[1]], xs[vars[0]], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[1]} (cm)', ylabel=f'{vars[0]} (cm)',
               title=f'Dependencia Lineal ({vars[1]}, {vars[0]}).')
        ax.legend(loc='best')
        fig.savefig(f'{str}.pdf')
        plt.show()
        dicto = {"Coeffs": reg[0], "Errs": [np.sqrt((reg[1])[0, 0]), np.sqrt((reg[1])[1, 1])], "Rsq": R_sq}
    else:
        n = int(str[-1])
        reg = np.polyfit((xs[n])[vars[1]], (xs[n])[vars[0]], deg=1, full=False, cov=True)
        corr_matrix = np.corrcoef((xs[n])[vars[1]], (xs[n])[vars[0]])
        corr = corr_matrix[0, 1]
        R_sq = corr ** 2
        trend = np.polyval(reg[0], (xs[n])[vars[1]])
        fig, ax = plt.subplots()
        ax.set_axisbelow(True)
        ax.grid(color='gray', linestyle='-.', linewidth=0.5)
        ax.plot((xs[n])[vars[1]], trend, 'r',
                label=f'{vars[0]}= %.5f $\cdot$ {vars[1]} + (%.3f); $R^2$ = %.3f' % ((reg[0])[0], (reg[0])[1], R_sq))
        ax.scatter((xs[n])[vars[1]], (xs[n])[vars[0]], label='Puntos Experimentales')
        ax.set(xlabel=f'{vars[1]} (cm)', ylabel=f'{vars[0]} (cm)',
               title=f'Dependencia Lineal ({vars[1]}, {vars[0]}). Paquete de medidas {n + 1}')
        ax.legend(loc='best')
        fig.savefig(f'Figura{n}.pdf')
        plt.show()
        dicto = {"Coeffs": reg[0], "Errs": [np.sqrt((reg[1])[0, 0]), np.sqrt((reg[1])[1, 1])], "Rsq": R_sq}
    return dicto

#6.- Find Lambda
def lamda(n):
    slope = (plot(doms,f'Figura {n}')['Coeffs'])[0]
    lamda = slope*(((datas[n])[0])[4])
    return lamda

def lamdaerr(n):
    slope = (plot(doms, f'Figura {n}')['Coeffs'])[0]
    errslope = (plot(doms, f'Figura {n}')['Errs'])[0]
    lamdaerr = errslope*(((datas[n])[0])[4]) + slope*(((datas[n])[0])[5])
    return lamdaerr
res = list(map( lambda x: plot(doms,'Figura %i'%(x)),[0,1,2,3]))
reslamda = list(map(lamda,[0,1,2,3]))
reslamdaerr = list(map(lamdaerr,[0,1,2,3]))
avglamda = sum(reslamda)/(len(reslamda))
avglamdaerr = sum(reslamdaerr)/(len(reslamda))


#7.- Final regression
l = list()
for i in range(0,4):
    l.append(pospant-(48.9 - i) + e_bip_pant)
a = list()
for i in range(0,4):
    a.append(L-l[i])
e_a = e_L + 0.6
hs = list()
for i in range(0,4):
    hs.append(((datas[i])[0])[4])
dom = {"h":hs,"a":a}
resfin = plot(dom,"Dependencia Lineal (a,h)")
eta = 1.5
alpha = 0.5*(resfin['Coeffs'][0])*(1/(eta-1))
alpha_err = 0.5*(resfin['Errs'][0])*(1/(eta-1))
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
A = {}
A["s"] = list()
A["spri"] = list()
A["beta"] = list()
for _ in range(0,4):
    A["s"] += list(map(lambda x: print_error(preim_gauss(x,fpri)[0],preim_gauss(x,fpri)[1]), spriset))
    A["spri"] += list(map(lambda x: print_error(x,0.6), spriset))
    A["beta"] += list(map(lambda x: print_error(preim_gauss(x,fpri)[2],preim_gauss(x,fpri)[3]), spriset))
A["hprisndelxpris"] = list(map(lambda x: print_error(x,0.005), hpriset1 + hpriset2 + hpriset3 + hpriset4))
A["hsndelx"] = list()
A["asnDs"] = list()
for i in range(0,4):
    A["hsndelx"] += list(map(lambda n: print_error(((datas[i])[n])[4],((datas[i])[n])[5]), list(range(0,10))))
    A["asnDs"] += list(map(lambda n: print_error(((datas[i])[n])[6], ((datas[i])[n])[7]), list(range(0, 10))))

def csvfile(n):
    with open(f'table {n}.csv', 'w+', newline='') as f:  # You will need 'wb' mode in Python 2.x
        w = csv.DictWriter(f, A.keys())

        for i in range(10*n, 10*(n+1)):
            line = {}
            for j in list(A.keys()):
                line[j] = (A[j])[i]
            w.writerow(line)

for i in range(0,4):
    csvfile(i)
