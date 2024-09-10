''''Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul
fiecărei reprezentări cromozomiale;
b.Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin inserare care, pe baza populaţiei pop
obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi.'''

import numpy as np

 #candidat:1,0,2,3,4 int_min=2 int_max=4 --> copil:1,0,4,2,3
t=[1,0,2,3,4]

def fitness(candidat):
    scor=0
    for i in range(len(candidat)-1):
        for j in range(i+1,len(candidat)):
            if candidat[i]==j and candidat[j]==i:
                scor=scor+1
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n+1],dtype=int)
    candidat=[]
    for i in range(dim):
        candidat=np.random.permutation(n)
        pop[i][0:n]=candidat #de la 0 la n-1
        pop[i][n]=fitness(candidat) #pe pozitia n (ultima pozitie)
    return pop

def mutatie_inserare(pop,dim,pm):
    popm=pop.copy()
    interval=np.random.randint(0,len(pop[0])-1,2)
    if interval[0]==interval[1]:
        interval = np.random.randint(0, len(pop[0]) - 1, 2)
    interval_min=min(interval)
    interval_max=max(interval)
    for i in range(dim):
        candidat=popm[i]
        r=np.random.uniform(0,1)
        if r<=pm:
            print("Candidat initial:",candidat)
            copil=candidat.copy()
            copil[interval_min+1]=candidat[interval_max] #daca sunt = nu afecteaza cu nimic
            #verific 1. daca interval_min este penultimul interval--> interval_min+1 este deja interval_max deci nu mai fac inserarea(nu afecteaza cu nimic)
            #        2. daca interval_min este deja pe ultima pozitie --> nu se face inserarea
            #candidat[.,.,i,i+1,.,.,.,j] copil[.,.,i,j,i+2(=i+1 din candidat pt ca mut elementele spre dreapta)
            if interval_min<(len(candidat)-3):
                copil[interval_min+2:(len(candidat)-1)]=[candidat[j] for j in range(interval_min+1,(len(candidat)-1)) if j!=interval_max]
                print("Mutatie:", copil)
                copil[len(candidat)-1]=fitness(copil[0:(len(candidat)-1)])

    return popm

scor=fitness(t)
print(scor)
populatie=generare_populatie(20,6)
print(populatie)
popm=mutatie_inserare(populatie,20,0.1)
print(popm)