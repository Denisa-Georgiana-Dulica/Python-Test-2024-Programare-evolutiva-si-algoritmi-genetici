'''Consideram spatiul solutiilor unei porbleme format din permutarile de dimensiune k. Calitatea unui individ P
este data de nr perechilor (i,i+1) pentru care P(i)=i+1 P(i+1)=i
a)generare pop, vector de calitate
b)pentru o prob de incrutisare data (recombinare) scrieti o functie de recombinare utilizand operatorul OCX
care pe baza populatiei pop obtine o noua populatie, copii.Populatia rezultata are tot dim indivizi'''
import numpy as np
def fitness(candidat):
    scor=0
    for i in range(len(candidat)-1):
        for j in range(i+1,len(candidat)):
            if candidat[i]==j and candidat[j]==i:
                scor+=1
    return scor

def generare_populatie(dim,k):
    pop=np.zeros([dim,k])
    vector_calitate=np.zeros(dim)
    for i in range(dim):
        pop[i]=np.random.permutation(k)
        vector_calitate[i]=fitness(pop[i])
    return pop,vector_calitate


'''def secventa_copiat(pop,dim,pc,vector_calitati,k):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i]
        p2=popc[i+1]
        r=np.random.uniform(0,1)
        if r<=pc:
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            pozitii=np.random.randint(0,k,2)
            if pozitii[0]==pozitii[1]:
                pozitii = np.random.randint(0, k, 2)
            minim=min(pozitii)
            maxim=max(pozitii)
            copil1=OCX(p1,p2,minim,maxim,k)
            copil2= OCX(p2, p1, minim, maxim, k)
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i+1] = copil2
            popc[i]=copil1
            vector_calitati[i]=fitness(copil1)
            vector_calitati[i+1] = fitness(copil2)
    return popc
def OCX(p1,p2,min,max,k):
    copil_secventa=[p1[i] for i in range(min,max+1)]
    valori_final=[p2[i] for i in range(max,k) if p2[i] not in copil_secventa]
    valori_inceput = [p2[i] for i in range(0,max) if p2[i] not in copil_secventa]
    valori=np.append(valori_final,valori_inceput)
    copil_final=[valori[i] for i in range(k-max-1)]
    copil_inceput=[valori[i] for i in range(k-max-1,len(valori))]
    copil=np.append(copil_inceput,copil_secventa)
    copil_final=np.append(copil,copil_final)
    return copil_final'''

def secventa_copiat(pop,dim,pc,vector_calitati,k):
    popc = pop.copy()
    for i in range(0, dim - 1, 2):
        p1 = popc[i]
        p2 = popc[i + 1]
        r = np.random.uniform(0, 1)
        if r <= pc:
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            pozitii = np.random.randint(0, k, 2)
            if pozitii[0] == pozitii[1]:
                pozitii = np.random.randint(0, k, 2)
            minim = min(pozitii)
            maxim = max(pozitii)
            copil1 = PMX(p1, p2, minim, maxim, k)
            copil2 = PMX(p2, p1, minim, maxim, k)
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i + 1] = copil2
            popc[i] = copil1
            vector_calitati[i] = fitness(copil1)
            vector_calitati[i + 1] = fitness(copil2)
        return popc

def PMX(p1,p2,min,max,k):
    copil=-np.ones(k,dtype=int)
    copil[min:max+1]=p1[min:max+1]
    for i in range(min,max+1):
        a=p2[i]
        if a not in copil:
            curent=i
            plasat=False
            while not plasat:
                b=p1[curent]
                pozitie=[j for j in range(k) if p2[j]==b]
                if copil[pozitie]==-1:
                    copil[pozitie]=a
                    plasat=True
                else:
                    curent=pozitie
    valori_nefolosite=[p2[i] for i in range(k) if p2[i] not in copil]
    pozitii_goale=[i for i in range(k) if copil[i]==-1]
    m=len(pozitii_goale)
    for i in range(m):
        copil[pozitii_goale[i]]=valori_nefolosite[i]
    return copil


pop,vector_calitate=generare_populatie(10,5)
print(pop)
print(vector_calitate)
popc=secventa_copiat(pop,10,0.6,vector_calitate,5)
print(popc)