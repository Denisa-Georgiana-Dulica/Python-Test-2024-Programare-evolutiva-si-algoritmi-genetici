'''
Fie 𝑓:[−1,1]×[0,0.2]×[0,1]×[0,5]→ℝ, 𝑓(𝑥1,𝑥2,𝑥3)=1+𝑠𝑖𝑛(2𝑥1−𝑥3)+(𝑥2∗𝑥4)^(1/3)
funcţia obiectiv a unei probleme de maxim. Un genotip este un vector 𝑥= (𝑥1,𝑥2,𝑥3,𝑥4)𝑇,𝑥∈[−1,1]×[0,0.2]×[0,1]×[0,5]
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
b.Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie mutaţie de tip fluaj (adica mutatie neuniforma) cu pragul 𝑡=0.6 (𝜎=𝑡3) care, pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai lui pop.
'''

import numpy as np
#AVEM NUMERE REALE pop[i][0] = np.random.uniform(-1, 1)-->intervalul lui x1
#O SA AM UN VECTOR DE 4 ELEMENTE PENTRU CA AM 4 X
#POPULATIE ALCATUITA DIN VECTORI DE X

#MUTATIE NEUNIFORMA=fluaj cu sigma
#o sa aleg din candidat random orice valoare(gena) - pozitie
#o sa aleg o valoare random intre 0 si sigma
#la candidat[pozitie] adaug acea valoare

def fitness(candidat):
    scor=1+np.sin(2*candidat[0]-candidat[2])+(candidat[1]*candidat[3])**(1/3)
    return scor

#cerinta a
def generare_populatie(dim):
   pop=np.zeros([dim,4]) #4 pentru ca sunt 4 de x si avem default float
   calitate=np.zeros(dim)
   for i in range(dim):
       pop[i][0] = np.random.uniform(-1, 1)  # uniform pt ca sunt nr reale
       pop[i][1] = np.random.uniform(0, 0.2)
       pop[i][2] = np.random.uniform(0, 1)
       pop[i][3] = np.random.uniform(0, 5)
       calitate[i]=fitness(pop[i])
   return pop,calitate


def mutatie_neuniforma(pop,dim,pm,sigma,calitate): #noua ni se da sigma=0.6
    popm=pop.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            # aleg random o pozitie din candidat
            pozitie = np.random.randint(0, len(pop[0]))
            # aleg random o valoare intre 0 si sigma
            valoare_adaugata = np.random.normal(0, sigma)
            print("Candidat:",popm[i])
            candidat=popm[i]
            if pozitie==0:
                candidat[pozitie]=candidat[pozitie]+valoare_adaugata
                if candidat[pozitie]<-1:
                    candidat[pozitie] = -1
                elif candidat[pozitie]>1:
                    candidat[pozitie] = 1
            if pozitie==1:
                candidat[pozitie]=candidat[pozitie]+valoare_adaugata
                if candidat[pozitie]<0:
                    candidat[pozitie] = 0
                elif candidat[pozitie]>0.2:
                    candidat[pozitie] = 0.2
            if pozitie==2:
                candidat[pozitie]=candidat[pozitie]+valoare_adaugata
                if candidat[pozitie]<0:
                    candidat[pozitie] = 0
                elif candidat[pozitie]>1:
                    candidat[pozitie] = 1
            if pozitie==3:
                candidat[pozitie]=candidat[pozitie]+valoare_adaugata
                if candidat[pozitie]<0:
                    candidat[pozitie] = 0
                elif candidat[pozitie]>5:
                    candidat[pozitie] = 5
            print("Mutatie:",popm[i])
            calitate[i]=fitness(popm[i])
            print("Calitate noua:",calitate[i])
    return popm


pop,calitate=generare_populatie(20)
print("Populatia:\n",pop)
print("Calitate:",calitate)
popm=mutatie_neuniforma(pop,20,0.1,0.6,calitate)
print(popm)