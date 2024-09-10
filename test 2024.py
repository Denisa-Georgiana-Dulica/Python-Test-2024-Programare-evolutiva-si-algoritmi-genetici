import numpy as np

def fitness(candidat):
    scor=0
    for i in range(len(candidat)):
        if candidat[i]==i:
            scor+=1
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n],dtype=int)
    vector_calitate=np.zeros(dim)
    for i in range(dim):
        pop[i]=np.random.permutation(n)
        vector_calitate[i]=fitness(pop[i])
    return pop,vector_calitate

def selectare_poz(pop,vector_calitate,dim,n,pc):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i]
        p2=popc[i+1]
        r=np.random.uniform(0,1)
        if r<=pc:
            interval=np.random.randint(0,n,2)
            if interval[0]==interval[1]:
                interval = np.random.randint(0, n, 2)
            minim=min(interval)
            maxim=max(interval)
            print("p 1:", p1)
            print("p 2:", p2)
            copil1=OCX(p1,p2,minim,maxim,n)
            copil2= OCX(p2, p1, minim, maxim, n)
            print("copil 1:",copil1)
            print("copil 2:", copil2)
            popc[i]=copil1
            vector_calitate[i]=fitness(copil1)
            popc[i+1]=copil2
            vector_calitate[i+1] = fitness(copil2)
    return popc

def OCX(p1,p2,min,max,n):
    copil_selectie=[p1[i] for i in range(min,max+1)]
    valori_final=[p2[i] for i in range(max,n) if p2[i] not in copil_selectie]
    valori_inceput=[p2[i] for i in range(0,max) if p2[i] not in copil_selectie]
    valori=np.append(valori_final,valori_inceput)
    copil_final=[valori[i] for i in range(n-max-1)]
    copil_inceput = [valori[i] for i in range(n - max - 1,len(valori))]
    c=np.append(copil_inceput,copil_selectie)
    copil=np.append(c,copil_final)
    return copil


pop,vector_calitate=generare_populatie(15,10)
print(pop)
popc=selectare_poz(pop,vector_calitate,15,10,0.6)
print(popc)