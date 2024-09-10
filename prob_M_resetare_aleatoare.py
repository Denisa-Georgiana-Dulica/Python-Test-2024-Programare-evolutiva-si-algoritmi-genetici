'''Fie 𝑓:{1,2,…,1500}×{−1,0,,…,2500}→ℝ,𝑓(𝑥,𝑦)=𝑦∗(𝑠𝑖𝑛(𝑥−2))^2
funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip (𝑥,𝑦)∈{1,2,…,1500}×{−1,0,…,2500}
'''
import numpy as np
def fitness(candidat):
    scor=0
    scor=candidat[1]*((np.sin(np.deg2rad(candidat[0]-2)))**2)
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,2],dtype=int)
    calitate=np.zeros(dim)
    for i in range(dim):
        pop[i][0]=np.random.randint(1,1501)
        pop[i][1] = np.random.randint(-1, 2501)
        calitate[i]=fitness(pop[i])
    return pop,calitate

def mutatie_resetare_aleatoare(pop,dim,pm,calitate):
    popm=pop.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            candidat=popm[i]
            print("Candidat initial:", candidat)
            pozitie=np.random.randint(0,len(pop[0]))
            if pozitie==0:
                candidat[pozitie]=np.random.randint(1,1501)
            if pozitie==1:
                candidat[pozitie] = np.random.randint(-1, 2501)
            print("Mutatie:", candidat)
            calitate[i] = fitness(candidat)
            print("Calitate noua:", calitate[i])
        return popm


pop,calitate=generare_populatie(5)
print(pop)
print(calitate)
popm=mutatie_resetare_aleatoare(pop,5,0.1,calitate)
