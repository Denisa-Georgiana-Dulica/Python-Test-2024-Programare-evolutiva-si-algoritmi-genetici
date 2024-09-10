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

def secventa_copiata_OCX(pop,dim,pc,n):
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:n]
        p2=popc[i+1][0:n]
        r=np.random.uniform(0,1)
        if r<=pc:
            poz=np.random.randint(0,n,2)
            if poz[0]==poz[1]:
                poz = np.random.randint(0, n, 2)
            int_min=min(poz)
            int_max=max(poz)
            print("max:",int_max)
            print("min:",int_min)
            print("Parinte 1:",p1)
            print("Parinte 2:", p2)
            copil1=OCX(p1,p2,int_max,int_min,n)
            copil2 = OCX(p2, p1, int_max, int_min, n)
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            popc[i][0:n] = copil1
            popc[i][n] = fitness(copil1)
            popc[i + 1][0:n] = copil2
            popc[i + 1][n] = fitness(copil2)
            print("Fitness 1:", popc[i][n])
            print("Fitness 2:", popc[i + 1][n])
    return popc

def OCX(parinte1, parinte2,max,min,n):
    #copiez secventa din parintele 1 in copilul 1
    copil_secventa=[parinte1[i] for i in range(min,max+1)] #lista
    #aflu valorile din parintele 2 (incepand cu poz max pana la final) care nu se afla deja in copil
    valori_final=[parinte2[i] for i in range(max,n) if parinte2[i] not in copil_secventa] #lista
    # aflu valorile din parintele 2 (incepand cu 0 pana la max) care nu se afla deja in copil
    valori_inceput=[parinte2[i] for i in range(0,max) if parinte2[i] not in copil_secventa] #lista
    #incepand cu valorile de la final fac un vector cu valorile care nu se regasesc in copil
    valori=np.append(valori_final,valori_inceput)
    #o sa adaug intr-o lista primele nr din vectorul 'valori' = cu nr de locuri libere din copil de la max+1 pana la final
    copil_final=[valori[i] for i in range(n-max-1)] #AICI TREBUIE -1
    # o sa adaug intr-o lista nr ramase din vectorul 'valori' = cu nr de locuri libere din copil de la 0 pana la min
    copil_inceput=[valori[i] for i in range(n-max-1,len(valori))]
    #unesc primii vectori (in append pot sa folosesc doar 2
    c=np.append(copil_inceput,copil_secventa)
    copil=np.append(c,copil_final)
    return copil

pop=generare_populatie(10,6)
print(pop)
popc=secventa_copiata_OCX(pop,10,0.6,6)
print(popc)