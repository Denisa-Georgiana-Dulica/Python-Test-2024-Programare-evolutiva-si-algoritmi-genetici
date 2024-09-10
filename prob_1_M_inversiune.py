''''
S1. Fie f:P(n)→N, pϵP(n),f(p)=∑_(i=0)^(n-1)▒〖p_i*〖câștig〗_i 〗 funcţia obiectiv a unei probleme de maxim, unde P(n) desemnează
mulţimea permutărilor de n elemente și câștig este un vector de intrare, cu n elemente, în care fiecare valoare arată câștigul unei alegeri .
	a) Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată
	într-un vector calitate;
	b)Pentru o probabilitate de mutaţie dată, pm,  scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin inversiune care,
	pe baza populaţiei pop obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi.
'''


import numpy as np
#numere naturale (intregi)
#am o multime de n permutari si un vector de castiguri care are un nr de elemente = nr de permutari din multime
#permutare(candidat) 1 --> castig[1]

n=7
castiguri=[10,20,30,40,50,60,70]
#cerinta a
def fitness(candidat):
    scor=0
    for i in range(len(candidat)):
        scor=scor+candidat[i]*castiguri[i]
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n+1],dtype=int)
    for i in range(dim):
        candidat = np.random.permutation(n)
        pop[i][0:n]=candidat
        pop[i][n]=fitness(candidat)
    return pop

#cerinta b
#prob de mutatie pm =0.1
def mutatie_inversiune(pm,pop,dim): #popm este populatia de copii (mutata)
    popm=pop.copy() #nu uita de paranteze
    interval=np.random.randint(0,len(pop[0])-1,2) #len(pop[0]-1) pentru ca pe ultima pozitie am calitatea
    if interval[0]==interval[1]:
        interval = np.random.randint(0, len(pop[0])-1, 2)
    interval_min=min(interval)
    interval_max = max(interval)
    candidat=[]
    for i in range(dim): #pentru fiecare individ (permutari) aleg r
        r=np.random.uniform(0,1)
        candidat=popm[i]
        if r<=pm:
            print("Candidat initial:", candidat)
            candidat[interval_min:interval_max+1]=[candidat[i] for i in range(interval_max,interval_min-1,-1)]
            print("Mutatie",candidat[interval_min:interval_max+1])
            #nu uita sa actualizezi si calitatea
            calitate_nou=fitness(candidat[0:len(pop[0])-1])
            candidat[len(pop[0])-1]=calitate_nou
            print("Calitate:",candidat[len(pop[0])-1])
    return popm


populatie=[]
populatie=generare_populatie(20,7)
print(populatie)
popm=mutatie_inversiune(0.1,populatie,20)
print(popm)