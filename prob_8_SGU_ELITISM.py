'''	Fie 𝑓:𝒫(𝑛)→ℕfuncţia obiectiv definită pentru problema celor n regine astfel: 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=𝑛×𝑛-1/2−|{(𝑖,𝑗)𝑖<𝑗,|𝑝(𝑖)−𝑝(𝑗)|=|𝑖−𝑗|⁄}|,
unde 𝒫(𝑛)desemnează mulţimea permutărilor de n elemente.
a)Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b)Aplicaţi funcţia de generare implementată mai sus pentru obţinerea a două populaţii, pop1, pop2 cu câte dim indivizi.
Scrieţi o funcţie Python care obţine o nouă populaţie prin aplicarea unei
proceduri de tip elitist celor două populaţii, unde
pop2 este considerată populaţia progeniturilor lui pop1. Populaţia rezultată are tot dim indivizi.
'''
import numpy as np
#PROBLEMA CELOR N REGINE
def fitness(candidat,nr_regine): #nr_regine = nr de elem din permutare
   scor_maxim=(nr_regine*(nr_regine-1))/2
   for i in range(0,nr_regine-1):
       for j in range(i+1, nr_regine):
           if(abs(i-j)==abs(candidat[i]-candidat[j])):
               scor_maxim-=1
   return scor_maxim

def generare_populatie(dim,nr_regine):
    pop=np.zeros([dim,nr_regine+1],dtype=int)
    for i in range(dim):
        pop[i][0:nr_regine]=np.random.permutation(nr_regine)
        pop[i][nr_regine]=fitness( pop[i][0:nr_regine],nr_regine)
    return pop

def elitism(pop_curenta, pop_copii,dim,nr_regine):
    copii=pop_copii.copy()
    calitati_pcurenta=np.zeros(dim)
    calitati_pcopii = np.zeros(dim)
    for i in range(dim):
        calitati_pcurenta[i]=pop_curenta[i][nr_regine]
        calitati_pcopii[i] = copii[i][nr_regine]
    max_curenta=max(calitati_pcurenta)
    max_copii=max(calitati_pcopii)
    if max_curenta>max_copii:
        pozitii_c=[i for i in range(nr_regine) if calitati_pcurenta[i]==max_curenta]
        pozitie_c=pozitii_c[0]
        pozitie_copil=np.random.randint(0,nr_regine)
        print("Copil initial:", copii[pozitie_copil])
        copii[pozitie_copil][0:nr_regine]=pop_curenta[pozitie_c][0:nr_regine]
        print("Copil nou:", copii[pozitie_copil])
        copii[pozitie_copil][nr_regine]=calitati_pcurenta[pozitie_c]
    return copii

pop_curenta=generare_populatie(5,5)
print("Populatia curenta:\n",pop_curenta)
pop_copii=generare_populatie(5,5)
print("Populatia copii:\n",pop_copii)
pop_noua=elitism(pop_curenta,pop_copii,5,5)
print("Populatia noua:\n",pop_noua)
