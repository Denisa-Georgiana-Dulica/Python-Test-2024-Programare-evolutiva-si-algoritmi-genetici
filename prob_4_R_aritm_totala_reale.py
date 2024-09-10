'''1.	Fie 𝑓:[−1,1]×[0,1]×[−2,1]→ℝ, 𝑓(𝑥1,𝑥2,𝑥3)=1+𝑠𝑖𝑛(2𝑥1−𝑥3)+𝑐𝑜𝑠(𝑥2)funcţia obiectiv a unei probleme de maxim.
Un genotip este un vector 𝑥=(𝑥1,𝑥2,𝑥3)𝑇,𝑥∈[−1,1]×[0,1]×[−2,1]
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
indivizii populaţiei sunt însoţiţi de funcţia merit (sunt vectori cu 4 componente).
b.Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de recombinare aritmetică
totală care, pe baza populaţiei pop obţine o nouă populaţie, popc.
Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la
sfârşitul fiecărei reprezentări cromozomiale).'''
import numpy as np

def fitness(x):
    return 1+2*np.sin(x[0]-x[2])+np.cos(x[1])

def generare_populatie(dim):
    populatie=np.zeros([dim,4])
    for i in range(dim):
        populatie[i][0]=np.random.uniform(-1,1)
        populatie[i][1]= np.random.uniform(0, 1)
        populatie[i][2] = np.random.uniform(-2, 1)
        populatie[i][3]=fitness(populatie[i][0:3])
    return populatie


'''def recombinare_arit_totala(pop,dim,pc,alpha):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:3]
        p2 = popc[i+1][0:3]
        r=np.random.uniform(0,1)
        if r<=pc:
            copil1=p1.copy()
            copil2=p2.copy()
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            #iau fiecare valoare din copii si aplic aceasta formula
            for j in range(3):
                copil1[j]=alpha*p1[j]+(1-alpha)*p2[j]
                copil2[j]=alpha*p2[j]+(1-alpha)*p1[j]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
        popc[i][0:3]=copil1
        popc[i][3] = fitness(copil1)
        popc[i+1][0:3]=copil2
        popc[i+1][3] = fitness(copil2)
        print("Fitness 1:", popc[i][3])
        print("Fitness 2:", popc[i + 1][3])
    return popc'''

'''def recombinare_arit_simpla(pop,dim,pc,alpha):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:3]
        p2 = popc[i+1][0:3]
        r=np.random.uniform(0,1)
        if r<=pc:
            copil1=p1.copy()
            copil2=p2.copy()
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            i=np.random.randint(0,3)
            for j in range(i,3):
                copil1[j]=alpha*p1[j]+(1-alpha)*p2[j]
                copil2[j]=alpha*p2[j]+(1-alpha)*p1[j]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
        popc[i][0:3]=copil1
        popc[i][3] = fitness(copil1)
        popc[i+1][0:3]=copil2
        popc[i+1][3] = fitness(copil2)
        print("Fitness 1:", popc[i][3])
        print("Fitness 2:", popc[i + 1][3])
    return popc'''

def recombinare_arit_singulara(pop,dim,pc,alpha):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:3]
        p2 = popc[i+1][0:3]
        r=np.random.uniform(0,1)
        if r<=pc:
            copil1=p1.copy()
            copil2=p2.copy()
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            #iau fiecare valoare din copii si aplic aceasta formula
            i = np.random.randint(0, 3)
            copil1[i]=alpha*p1[i]+(1-alpha)*p2[i]
            copil2[i]=alpha*p2[i]+(1-alpha)*p1[i]
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
        popc[i][0:3]=copil1
        popc[i][3] = fitness(copil1)
        popc[i+1][0:3]=copil2
        popc[i+1][3] = fitness(copil2)
        print("Fitness 1:", popc[i][3])
        print("Fitness 2:", popc[i + 1][3])
    return popc

populatie=generare_populatie(10)
print(populatie)
popc=recombinare_arit_singulara(populatie,10,0.7,0.25)
print(popc)


