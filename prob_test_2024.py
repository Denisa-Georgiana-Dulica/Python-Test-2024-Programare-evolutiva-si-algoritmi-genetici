'''fie functia de maxim f:{x=(x1,...,x10) unde xi =[-1,1], x1+..+x9=1-x10} ->R
f(x)=a1*x1+...+a10*x10
a=(a1,...,a10) vector constant, data de intrare
a)generare populatie pop, calitatea fiecarui individ se afla intr-un vector de calitati
b)pt un pc dat, recombinare aritmetica simpla --> o noua populatie copii. Pop rezultata are tot dim indivizi.'''
import numpy as np
a=[1,2,3,4,5,6,7,8,9,10]

def fitness(x,a):
    scor=0
    for i in range(len(a)):
        scor+=x[i]*a[i]
    ok=False
    if x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]>=1-x[9]:
        ok=True
    return scor,ok

def generare_populatie(dim):
    pop=np.zeros([dim,10])
    calitate=np.zeros(dim)
    i=0
    while i<dim:
        j=0
        while j<10:
            pop[i][j]=np.random.uniform(-1,1)
            j=j+1
        valoare,ok=fitness(pop[i],a)
        if ok==True:
            calitate[i]=valoare
            i=i+1
    return pop,calitate

def recombinare_aritmetica_simpla(pop,dim,pc,calitate):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:10]
        p2= popc[i+1][0:10]
        r=np.random.uniform(0,1)
        if r<=pc:
            copil1=p1.copy()
            copil2=p2.copy()
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            i=np.random.randint(0,10)
            copil1[i:10]=p2[i:10]
            copil2[i:10] = p1[i:10]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            valoare1,ok1=fitness(copil1,a)
            if ok1==True:
                calitate[i]=valoare1
                print("Calitate copil 1:",calitate[i])
            else:
                popc[i]=pop[i].copy()
            valoare2, ok2 = fitness(copil2, a)
            if ok2 == True:
                calitate[i+1] = valoare2
                print("Calitate copil 2:", calitate[i+1])
            else:
                popc[i+1] = pop[i+1].copy()

    return popc


pop,calitate=generare_populatie(10)
print(pop)
print(calitate)
popc=recombinare_aritmetica_simpla(pop,10,0.6,calitate)
print(popc)