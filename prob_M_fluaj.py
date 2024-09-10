'''Fie 𝑓:{1,2,…,1500}×{−1,0,,…,2500}→ℝ,𝑓(𝑥,𝑦)=𝑦∗(𝑠𝑖𝑛(𝑥−2))^2
funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip (𝑥,𝑦)∈{1,2,…,1500}×{−1,0,…,2500}
'''

#NUMERE INTREGI
#MUTATIE FLUAJ
#aleg o pozitie random si la acea valoare +1 sau -1
import numpy as np

def fitness(candidat):
    scor=0
    #np.sin nu da la fel ca sin de pe calculator
    scor=candidat[1]*(np.sin(candidat[0]-2))**2
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,2])
    calitate=np.zeros(dim)
    for i in range(dim):
        pop[i][0]=np.random.randint(1,1501)
        pop[i][1]=np.random.randint(-1,2501)
    for i in range(dim):
        calitate[i]=fitness(pop[i])
    return pop,calitate

def mutatie_fluaj(pop,pm,dim,calitate):
    popm=pop.copy()
    for i in range(dim):
        candidat=popm[i]
        r=np.random.uniform(0,1)
        if r<=pm:
            #aleg pozitia
            pozitie = np.random.randint(0, len(popm[0]))
            #aleg un semn
            p = np.random.randint(0, 2)
            if p == 0:
                semn = -1
            elif p == 1:
                semn = 1
            print("Candidat initial:",candidat)
            #aleg in functie de interval
            if pozitie==0:
                candidat[pozitie]=candidat[pozitie]+semn
                if candidat[pozitie]<1:
                    candidat[pozitie]=1
                elif candidat[pozitie]>1500:
                    candidat[pozitie] = 1500
            if pozitie == 1:
                candidat[pozitie] = candidat[pozitie] + semn
                if candidat[pozitie] < -1:
                    candidat[pozitie] = -1
                elif candidat[pozitie] > 2500:
                    candidat[pozitie] = 2500
            print("Mutatie:",candidat)
            calitate[i]=fitness(candidat)
            print("Calitate noua:",calitate[i])
    return popm

pop,calitate=generare_populatie(5)
print(pop)
print(calitate)
popm=mutatie_fluaj(pop,0.1,5,calitate)
