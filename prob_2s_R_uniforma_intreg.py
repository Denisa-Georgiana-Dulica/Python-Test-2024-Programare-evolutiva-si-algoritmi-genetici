''' Fie f:{1,2,…,1500}×{-1,0,,…,2500}×{10,11,…,250}×{10,11,…,250}→R,
f(x,y,z,t)=〖y*(sin(x-2))〗^2+z+t funcţia obiectiv a unei probleme de maxim.
Un candidat la soluție (genotip) este un vector (x,y,z,t)∈{1,2,…,1500}×{-1,0,,…,2500}×{10,11,…,250}×{10,11,…,250}.
a)Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b)Pentru o probabilitate de recombinare dată, pc,  scrieţi o funcţie de recombinare utilizând operatorul de încrucişare uniform care,
pe baza populaţiei pop obţine o nouă populaţie, popc. Populaţia rezultată are tot dim indivizi
(este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale).'''
import numpy as np

def fitness(candidat):
    scor=0
    scor=candidat[1]*(np.sin(candidat[0]-1)**2)+candidat[2]+candidat[3]
    return scor

def generarePopulatie(dim):
    pop=np.zeros([dim,5],dtype=int)
    for i in range(dim):
        pop[i][0]=np.random.randint(1,1501)
        pop[i][1] = np.random.randint(-1, 2501)
        pop[i][2] = np.random.randint(10, 250)
        pop[i][3] = np.random.randint(10, 250)
        pop[i][4]=fitness(pop[i][0:4])
    return pop

def recombinare_uniforma(pop,dim,n,pc): #n=4 (4 elem +calitatea)
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=pop[i][0:n]
        p2=pop[i+1][0:n]
        r=np.random.uniform(0,1)
        if r<=pc:
            print("Parinte 1:", p1)
            print("Parinte 2:",p2)
            copil1=p1.copy()
            copil2=p2.copy()
            for j in range(n): #pentru fiecare valoare din fiecare copil generez o valoare care e fie 0 fie 1, daca este 1 --> se face recombinarea
                valoare=np.random.randint(0,2)
                if valoare==1:
                    copil1[j]=p2[j]
                    copil2[j]=p1[j]
            print("Copil 1:",copil1)
            print("Copil 2:",copil2)
            popc[i][0:n]=copil1
            popc[i][n]=fitness(copil1)
            popc[i+1][0:n] = copil2
            popc[i+1][n] = fitness(copil2)
            print("Fitness 1:", popc[i][n])
            print("Fitness 2:",  popc[i+1][n])
    return popc

pop=generarePopulatie(10)
print(pop)
popc=recombinare_uniforma(pop,10,4,0.6)
print(popc)