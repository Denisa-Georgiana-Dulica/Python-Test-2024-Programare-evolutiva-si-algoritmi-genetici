'''S3. Fie funcţia f(x)=∑_Xi ,x=(x_1,…,x_17 )∈{0,1}^17, x cu număr par de biți 1, care trebuie
maximizată (un genotip este un vector binar cu 17 componente și număr par de biți 1).
	Scrieţi o funcţie Python  pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
	calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
	Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea
	selecţiei de tip turneu cu k indivizi (k parametru de intrare).

'''
import numpy as np
def fitness(candidat):
    scor=0
    nr_biti_1=0
    for i in range(len(candidat)):
        scor+=candidat[i]
        if candidat[i]==1:
            nr_biti_1+=1
    ok=False
    if nr_biti_1%2==0:
        ok=True
    return scor,ok

def generare_populatie(dim):
    pop=np.zeros([dim,17+1],dtype=int)
    i=0
    while i<dim:
        for j in range(17):
            pop[i][j]=np.random.randint(0,2)
        calitate,ok=fitness(pop[i][0:17])
        if ok==True:
            pop[i][17]=calitate
            i+=1
    return pop
def sortare(pop,vector_calitati):
    indici=np.argsort(vector_calitati)
    pop_sortata=pop[indici]
    vector_calitati_sortat=vector_calitati[indici]
    return pop_sortata,vector_calitati_sortat
def genitor(pop_curenta,pop_copii,dim,nr_inlocuiri):
    parinti=np.zeros([dim,17],dtype=int)
    for i in range(dim):
        parinti[i][0:17]=pop_curenta[i][0:17]
    vector_calitati = np.zeros(dim)
    for i in range(dim):
        vector_calitati[i] = pop_curenta[i][17]

    p, c = sortare(parinti, vector_calitati)
    poz = np.random.randint(0, dim, nr_inlocuiri)
    for j in range(nr_inlocuiri):
        p[j][0:17] = pop_copii[poz[j]][0:17]
        c[j] = vector_calitati[poz[j]]
        print(poz[j])
    amestec = np.random.permutation(dim)
    pop_urm = p[amestec]
    vector = c[amestec]
    return pop_urm




pop1=generare_populatie(10)
print(pop1)
pop2=generare_populatie(10)
print(pop2)
pop_urm=genitor(pop1,pop2,10,2)
print("gen urm:\n",pop_urm)