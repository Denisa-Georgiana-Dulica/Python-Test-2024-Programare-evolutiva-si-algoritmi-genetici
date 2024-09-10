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

def sortare(pop,vector_calitati):
    pozitii=np.argsort(vector_calitati)
    populatie_sortata=pop[pozitii]
    vector_calitati_sortate=vector_calitati[pozitii]
    return populatie_sortata,vector_calitati_sortate

def sel_determinista(pop_curenta,pop_copii,dim,nr_regine):
   populatie_curenta=np.zeros([dim,nr_regine],dtype=int)
   for i in range(dim):
       populatie_curenta[i][0:nr_regine]=pop_curenta[i][0:nr_regine]
   populatie_copii = np.zeros([dim, nr_regine],dtype=int)
   for i in range(dim):
       populatie_copii[i][0:nr_regine] = pop_copii[i][0:nr_regine]
   vector_cal_curenta=np.zeros(dim)
   for i in range(dim):
       vector_cal_curenta[i]=pop_curenta[i][nr_regine]
   vector_cal_copii = np.zeros(dim)
   for i in range(dim):
       vector_cal_copii[i] = pop_copii[i][nr_regine]

   p=np.append(populatie_curenta,populatie_copii)
   p.resize(2*dim,nr_regine)
   c=np.append(vector_cal_curenta,vector_cal_copii)
   p_sortat,c_sortat=sortare(p,c)
   print("Populatia sortata:\n", p_sortat)
   print("Vector cal sortat:\n", c_sortat)
   pop_finala=p[dim:2*dim].copy()
   calit_finala = c[dim:2 * dim].copy()

   amestec=np.random.permutation(dim)
   pop_finala_1=pop_finala[amestec]
   calit_finala_1=calit_finala[amestec]
   return pop_finala_1

pop_curenta=generare_populatie(10,5)
print("pop curenta:\n",pop_curenta)
pop_copii=generare_populatie(10,5)
print("pop copii:\n",pop_copii)
generatia_urm=sel_determinista(pop_curenta,pop_copii,10,5)
print("pop urmatoare:\n",generatia_urm)