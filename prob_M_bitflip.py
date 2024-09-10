'''Fie funcţia 𝑓(𝑥)=∑𝑥𝑖 𝑖=1..7,𝑥=(𝑥1,…,𝑥7)∈{0,1}care trebuie maximizată (un genotip este un vector binar cu 7 componente). '''
import numpy as np

def fitness(candidat):
    scor=0
    for i in range(len(candidat)):
        scor+=candidat[i]
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,7])
    calitate=np.zeros(dim)
    for i in range(dim):
        pop[i]=np.random.randint(0,2,7)
        calitate[i]=fitness(pop[i])
    return pop,calitate

def mutatie_bitflip(pop,dim,pm,calitate):
    popm=pop.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            candidat=popm[i]
            print("Candidat initial:", candidat)
            pozitie=np.random.randint(0,len(candidat))
            if candidat[pozitie]==0:
                candidat[pozitie]=1
            elif candidat[pozitie]==1:
                candidat[pozitie] = 1
            print("Mutatie:", candidat)
            calitate[i]=fitness(candidat)
            print("Calitate noua:", calitate[i])
    return popm

pop,calitate=generare_populatie(5)
print(pop)
print(calitate)
popm=mutatie_bitflip(pop,5,0.1,calitate)
print(popm)