'''11.
Fie 𝑓:{1,2,…,500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))^2−𝑥∙𝑐𝑜𝑠(2∙𝑥) funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip 𝑥 ={1, 2,.. 500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b.Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip turneu cu k
indivizi (k parametru de intrare).'''
import numpy as np
def baza10_baza2(candidat,nr_biti):
    sir_binar=bin(candidat)[2:]
    sir_final=sir_binar.zfill(nr_biti)
    vector_biti=np.zeros(nr_biti,dtype=int)
    for i in range(nr_biti):
        vector_biti[i]=int(sir_final[i])
    return list(vector_biti)

def baza2_baza10(vector_biti,nr_biti):
    sir_binar=''
    for i in range(nr_biti):
        sir_binar+=str(vector_biti[i])
    numar=int(sir_binar,2)
    return numar

def fitness(candidat,nr_biti):
    x=baza2_baza10(candidat,nr_biti)
    print(x)
    scor=0
    scor=(np.sin(x-2))**2-(x*np.cos(2*x))
    return scor

def generare_populatie(dim,nr_biti):
    pop=np.zeros([dim,nr_biti+1])
    for i in range(dim):
        x=np.random.randint(1,501)
        sir_binar=baza10_baza2(x,nr_biti)
        pop[i][0:nr_biti]=sir_binar
        pop[i][nr_biti]=fitness(sir_binar,nr_biti)
    return pop

def selectie_parinti_turneu(pop,dim,k,nr_biti): #k nr de parinti care intre in competitie
    parinti=pop.copy()
    for i in range(dim):
        poz=np.random.randint(0,dim,k)
        calitati_competitie=np.zeros(k)
        for j in range(k):
            calitati_competitie[j]=pop[poz[j]][nr_biti] #ultima valoare este calitatea
        maxim=max(calitati_competitie)
        pozitie_max=np.argmax(calitati_competitie)
        iselectie=poz[pozitie_max] #calitate_competitie si poz au acelasi j
        print("Castigator:",maxim)
        parinti[i][0:nr_biti]=pop[iselectie][0:nr_biti]
        parinti[i][nr_biti]=maxim
    return parinti



nr=baza10_baza2(500,9)
print(nr)
numar_10=baza2_baza10(nr,9)
print(numar_10)
calitate=fitness(nr,9)
print(calitate)

pop=generare_populatie(10,9)
print(pop)
parinti=selectie_parinti_turneu(pop,10,2,9)
print("Parinti:",parinti)



