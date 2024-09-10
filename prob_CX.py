''''d.	Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫 𝑛 desemnează mulţimea permutărilor de n elemente.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul
fiecărei reprezentări cromozomiale;
b.recombinare PMX
'''
import numpy as np

def fitness(candidat):
    scor=0
    for i in range(len(candidat)-1):
        for j in range(i+1,len(candidat)):
            if candidat[i]==j and candidat[j]==i:
                scor=scor+1
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n+1],dtype=int)
    for i in range(dim):
        pop[i][0:n]=np.random.permutation(n)
        pop[i][n]=fitness(pop[i][0:n])
    return pop


def crossover_CX(pop,dim,n,pc):
    popc = pop.copy()
    for i in range(0, dim - 1, 2):
        p1 = popc[i][0:n]
        p2 = popc[i + 1][0:n]
        r = np.random.uniform(0, 1)
        if r <= pc:
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            ciclu = cicluri(p1, p2, n)
            print("Ciclu:",ciclu)
            copil1 = p1.copy()
            copil2 = p2.copy()
            for j in range(n):
                cat, rest=np.divmod(ciclu[j],2) #impart valorile din ciclu=[1,1,2,3,1,1] la 2 si cel care are rest=0 --> ciclu par
                if rest == 0:
                    copil1[j] = p2[j]
                    copil2[j] = p1[j]

            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i][0:n] = copil1
            popc[i][n] = fitness(copil1)
            popc[i + 1][0:n] =copil2
            popc[i + 1][n] = fitness(copil2)
            print("Fitness 1:", popc[i][n])
            print("Fitness 2:", popc[i + 1][n])

        return popc


#DETERMIN CICLURILE
def cicluri(parinte1, parinte2,n):
    #fac un vector de nr 'ciclu' cu acest index ca sa retin in ce ciclu(par/impar) sunt valorile
    index=1
    ciclu=np.zeros(n)
    gata=0 #cand vectorul 'ciclu nu mai are valori=0 --> gata = 1'
    while not gata:
        #salvez pozitiile in clare ciclul este 0
        poz=np.where(ciclu==0) #initial o sa am poz=([0 1 2 3 4 5}, ) #ciclu tr sa fie ndarray
        if np.size(poz)!=0: #cat timp mai am valori =0
            i=poz[0][0] #i=0
            a=parinte1[i] #valoarea a va fi in ciclul 1 #valoarea a nu se schimba niciodata
            ciclu[i]=index
            b=parinte2[i]
            while b!=a:#daca valorile sunt = --> formeaza 1 ciclu
                pozitie=np.where(parinte1==b) #vad pe ce pozitie se afla b in parinte 1
                j=pozitie[0][0]
                ciclu[j]=index #valoarea de pe pozitia j se afla in ciclul 1
                b=parinte2[j] # caut urmatoarea valoare
            index+=1 #dupa ce b=a ies din bubla si trec la ciclul urmator =2
        else:
            gata=1 #cand nu mai am valori de 0 in ciclu
    return ciclu


pop=generare_populatie(10,6)
print(pop)
popc=crossover_CX(pop,10,6,0.6)
print(popc)