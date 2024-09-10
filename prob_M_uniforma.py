'''
Fie 𝑓:[−1,1]×[0,0.2]×[0,1]×[0,5]→ℝ, 𝑓(𝑥1,𝑥2,𝑥3)=1+𝑠𝑖𝑛(2𝑥1−𝑥3)+(𝑥2∗𝑥4)^(1/3)
funcţia obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥= (𝑥1,𝑥2,𝑥3,𝑥4)𝑇,𝑥∈[−1,1]×[0,0.2]×[0,1]×[0,5]
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b.Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie mutaţie de tip resetare aleatoare (adica mutatie uniforma) care, pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai lui pop.
'''
import numpy as np

#MUTATIE UNIFORMA = RESETARE ALEATOARE (FARA SIGMA)
#ALEG O POZITIE RANDOM DIN CANDIDAT SI O INLOCUIESC CU ALTA VALOARE DIN INTERVALUL LUI CANDIDAT[POIZTIE]

def fitness(candidat):
    scor=0
    scor=1+np.sin(2*candidat[0]-candidat[2])+(candidat[1]*candidat[3])**(1/3)
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,4])
    calitate=np.zeros(dim)
    for i in range(dim):
        pop[i][0]=np.random.uniform(-1,1)  #round(np.random.uniform(-1,1),3) rotunjire la 3 zecimale
        pop[i][1]=np.random.uniform(0,0.2)
        pop[i][2]=np.random.uniform(0,1)
        pop[i][3]=np.random.uniform(0,5)
        calitate[i]=fitness(pop[i])
    return pop,calitate

def mutatie_uniforma(pop,dim,pm,calitate):
    popm=pop.copy()
    for i in range(dim):
        candidat=popm[i]
        r=np.random.uniform(0,1)
        if r<=pm:
            pozitie = np.random.randint(0, len(pop[0]))
            print("Candidat initial:",candidat)
            if pozitie == 0:
                candidat[pozitie] = np.random.uniform(-1, 1)
            elif pozitie == 1:
                candidat[pozitie] = np.random.uniform(0, 0.2)
            elif pozitie == 2:
                candidat[pozitie] = np.random.uniform(0, 1)
            elif pozitie == 3:
                candidat[pozitie] = np.random.uniform(0, 5)
            print("Mutatie:",candidat)
            calitate[i]=fitness(candidat)
            print("Calitate noua:",calitate[i])
    return popm
pop,calitate=generare_populatie(20)
print("Populatia:\n",pop)
print("Calitate:",calitate)
popm=mutatie_uniforma(pop,20,0.1,calitate)
print(popm)