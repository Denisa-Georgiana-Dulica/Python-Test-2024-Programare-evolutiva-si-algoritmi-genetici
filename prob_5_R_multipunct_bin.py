'''Fie funcţia 𝑓(𝑥)=∑𝑥𝑖7𝑖=1,𝑥=(𝑥1,…,𝑥7)∈{0,1}care trebuie maximizată (un genotip este un vector binar cu 7 componente).
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este
memorată la sfârşitul fiecărei reprezentări cromozomiale;
b.Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare multi-punct
pentru 2 puncte de încrucişare care, pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi
(este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale)'''

import numpy as np
def fitness(candidat):
    scor=0
    for i in range(len(candidat)):
        scor+=candidat[i]
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,8],dtype=int)
    for i in range(dim):
        for j in range(7):
            pop[i][j]=np.random.randint(0,2)
        pop[i][7]=fitness(pop[i][0:7])
    return pop

def recombinare_multipunct_2pct(pop,dim,pc):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:7]
        p2=popc[i+1][0:7]
        r=np.random.uniform(0,1)
        if r<=pc:
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            copil1=p1.copy()
            copil2=p2.copy()

            m=np.random.randint(0,6)
            j=np.random.randint(m+1,7)

            copil1[m:j+1]=p2[m:j+1]
            copil2[m:j + 1] = p1[m:j + 1]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i][0:7]=copil1
            pop[i][7]=fitness(copil1)
            popc[i+1][0:7] = copil2
            pop[i+1][7] = fitness(copil2)
            print("Fitness 1:", popc[i][7])
            print("Fitness 2:", popc[i + 1][7])
    return popc

pop=generare_populatie(10)
print(pop)
popc=recombinare_multipunct_2pct(pop,10,0.6)
print(popc)