'''a.	Fie 𝑓:{1,2,…,350}→ℝ,𝑓(𝑥)+=xifuncţia obiectiv a unei probleme de maxim.
Fiecărui fenotip 𝑥∈{1,2,…,350}
'''

#RECOMBINARE UNIPUNCT PE NR INTREGI
import numpy as np
def fitness(candidat):
    scor=0
    for i in range(len(candidat)):
        scor+=candidat[i]
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n+1],dtype=int)
    for i in range(dim):
        for j in range(n):
            pop[i][j]=np.random.randint(1,351)
        pop[i][n]=fitness(pop[i][0:n])
    return pop

def recombinare_unipunct(dim,pc,pop,n):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:n]
        p2 = popc[i+1][0:n]
        r=np.random.uniform(0,1)
        if r<=pc:
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            copil1=p1.copy()
            copil2=p2.copy()
            j=np.random.randint(0,n-1)
            copil1[j:n]=p2[j:n]
            copil2[j:n] = p1[j:n]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i][0:n]=copil1
            popc[i][n]=fitness(copil1)
            popc[i+1][0:n]=copil2
            popc[i+1][n] = fitness(copil2)
            print("Fitness 1:", popc[i][n])
            print("Fitness 2:", popc[i + 1][n])
    return popc

pop=generare_populatie(10,4)
print(pop)
popc=recombinare_unipunct(10,0.6 ,pop,4)
print(popc)