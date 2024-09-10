'''	Fie 𝑓:𝒫(𝑛)→ℕfuncţia obiectiv definită pentru problema celor n regine astfel: 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=𝑛×𝑛-1/2−|{(𝑖,𝑗)𝑖<𝑗,|𝑝(𝑖)−𝑝(𝑗)|=|𝑖−𝑗|⁄}|,
unde 𝒫(𝑛)desemnează mulţimea permutărilor de n elemente. Scrieţi o funcţie Python pentru generarea
aleatoare a unei populaţii, pop, cu dimensiunea dim;
Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2. Scrieţi o funcţie
Python care obţine o nouă populaţie prin aplicarea unei proceduri de tip GENITOR (cu înlocuirea a 2 indivizi) celor
două populaţii, unde pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi.

'''
import numpy as np
def fitness(candidat,nr_regine):
    scor_maxim=(nr_regine*(nr_regine-1))/2
    for i in range(len(candidat)-1):
        for j in range(len(candidat)):
            if abs(i-j)==abs(candidat[i]-candidat[j]):
                scor_maxim-=1
    return scor_maxim

def generare_populatie(dim, nr_regine):
    pop=np.zeros([dim,nr_regine+1],dtype=int)
    for i in range(dim):
        pop[i][0:nr_regine]=np.random.permutation(nr_regine)
        pop[i][nr_regine]=fitness(pop[i][0:nr_regine],nr_regine)
    return pop

def sortare_populatie(pop,vector_calitati):
    indici_sortare=np.argsort(vector_calitati) #daca folosesc functia asta pe o matrice o sa imi returneze o matrice
    populatie_sortata=pop[indici_sortare]
    vector_calitati_sortat=vector_calitati[indici_sortare]
    return populatie_sortata,vector_calitati_sortat

def GENITOR(pop_curenta,pop_copii,dim,nr_regine):
    pop=np.zeros([dim,nr_regine],dtype=int)
    for i in range(dim):
        pop[i][0:nr_regine]=pop_curenta[i][0:nr_regine]
    vector_calitati = np.zeros(dim)
    for i in range(dim):
        vector_calitati[i] = pop_curenta[i][nr_regine]
    populatie_sortata,vector_calitati_sortat=sortare_populatie(pop,vector_calitati)
    print("Populatia sortata:\n",populatie_sortata)
    print("Vector cal sortat:\n", vector_calitati_sortat)
    pozitii=np.random.randint(0,dim,2)
    for i in range(2):
        populatie_sortata[i][0:nr_regine]=pop_copii[pozitii[i]][0:nr_regine]
        vector_calitati_sortat[i]=pop_copii[pozitii[i]][nr_regine]
        print("copii alesi:\n",populatie_sortata[i][0:nr_regine])
    amestec=np.random.permutation(dim) #atentie aici ordonez toti cei dim indivizi
    populatie_finala=populatie_sortata[amestec]
    calitati_finale=vector_calitati_sortat[amestec]
    return populatie_finala


pop_curenta=generare_populatie(10,5)
print("pop curenta:\n",pop_curenta)
pop_copii=generare_populatie(10,5)
print("pop copii:\n",pop_copii)
generatia_urm=GENITOR(pop_curenta,pop_copii,10,5)
print("pop urmatoare:\n",generatia_urm)
