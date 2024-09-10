''''d.  Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫 𝑛 desemnează mulţimea permutărilor de n elemente.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul
fiecărei reprezentări cromozomiale;
b.recombinare PMX
'''
import numpy as np

t=[1,0,3,4,5]

def fitness(candidat):
    scor=0
    #spune ca i<j --> i=0 j=1
    for i in range(len(candidat)-1):
        for j in range(i+1,len(candidat)):
            if candidat[i]==j and candidat[j]==i:
                scor=scor+1
    return scor

def generare_populatie(dim,n): #n = nr elemente din permutare
    pop=np.zeros([dim,n+1],dtype=int)
    for i in range(dim):
        candidat=np.random.permutation(n)
        pop[i][0:n]=candidat
        pop[i][n]=fitness(candidat)
    return pop

def secventa_comuna_pmx(pop,dim,n,pc):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:n]
        p2 = popc[i+1][0:n]
        r=np.random.uniform(0,1)
        if r<=pc:
            poz = np.random.randint(0, n, 2)
            while poz[0] == poz[1]:
                poz = np.random.randint(0, n, 2)
            interval_min = min(poz)
            interval_max = max(poz)
            print("max:",interval_max)
            print("min:",interval_min)
            print("Parinte 1:",p1)
            print("Parinte 2:", p2)
            copil1 =PMX(p1,p2,interval_min,interval_max,n)
            copil2 =PMX(p2,p1,interval_min,interval_max,n)
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i][0:n]=copil1
            popc[i][n]=fitness(copil1)
            popc[i+1][0:n] = copil2
            popc[i+1][n] = fitness(copil2)
            print("Fitness 1:", popc[i][n])
            print("Fitness 2:", popc[i+1][n])
    return popc

def PMX(parinte1,parinte2,min,max,n):
    copil=-np.ones(n,dtype=int)
    copil[min:max+1]=parinte1[min:max+1]
    for i in range(min,max+1):
        a=parinte2[i]
        if a not in copil:
            curent=i
            plasat=False
            while not plasat:
                b=parinte1[curent]
                poz=[j for j in range(n) if parinte2[j]==b]
                if copil[poz]==-1:
                    copil[poz]=a
                    plasat=True
                else:
                    curent=poz
    valori_necopiate=[parinte2[i] for i in range(n) if parinte2[i] not in copil]
    pozitii_libere=[i for i in range(n) if copil[i]==-1]
    m=len(pozitii_libere)
    for i in range(m):
        copil[pozitii_libere[i]]=valori_necopiate[i]
    return copil


pop=generare_populatie(10, 6)
print (pop)
popc=secventa_comuna_pmx(pop,10,6,0.6)
print(popc)

