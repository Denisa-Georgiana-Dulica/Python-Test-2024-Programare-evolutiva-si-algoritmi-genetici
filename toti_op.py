#RECOMBINARE PMX, OCX, CX
#SELECTIE PARINTI FPS SIGMA RULETA/SUS si SORTARE LRANG RULEZA/SUS
#SELECTIE GENERARTIE URM ELITISM GENITOR DETERMINISM
import numpy as np

def fitness(candidat):
    scor=0
    for i in range(len(candidat)-1):
        for j in range(i+1,len(candidat)):
            rezultat=candidat[i]-candidat[j]
            if (candidat[i] > candidat[j]) and ((rezultat % 2) == 0):
                scor=scor+1
    return scor

def generare_populatie(dim,n):
    pop=np.zeros([dim,n+1],dtype=int)
    for i in range(dim):
        permutare = np.random.permutation(n)
        pop[i][0:n] = permutare
        pop[i][n] = fitness(permutare)
    return pop

'''def crossover_PMX(populatie,dim,n,pc):
    pop=populatie.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        p1=pop[i][0:n]
        p2 = pop[i+1][0:n]
        if r<=pc:
            poz=np.random.randint(0,n,2)
            if poz[0]==poz[1]:
                poz = np.random.randint(0, n, 2)
            minim=min(poz)
            maxim=max(poz)
            print("Parinte 1:", p1)
            print("Parinte 2:", p2)
            copil1=PMX(p1,p2,minim,maxim,n)
            copil2 = PMX(p2, p1, minim, maxim, n)
            print("Copil 1:", copil1)
            print("Copil 2:", copil2)
            pop[i][0:n]=copil1
            pop[i + 1][0:n]=copil2
            pop[i][n]=fitness(copil1)
            pop[i+1][n] = fitness(copil2)
    return pop

def PMX(p1,p2,min,max,n):
    copil=-np.ones(n)
    copil[min:max+1]=p1[min:max+1]
    for i in range(min,max+1):
        a=p2[i]
        if a not in copil:
            curent=i
            plasat =False
            while not plasat:
                b=p1[curent]
                poz=[j for j in range(n) if p2[j]==b]
                pozitie=poz[0]
                if copil[pozitie]==-1:
                    copil[pozitie]=a
                    plasat=True
                else:
                    curent=pozitie

    valori_necompletate=[p2[i] for i in range(n) if p2[i] not in copil]
    pozitii_libere=[i for i in range(n) if copil[i]==-1]
    m=len(pozitii_libere)
    for i in range(m):
        copil[pozitii_libere[i]]=valori_necompletate[i]
    return copil'''

'''def cicluri(pop_curenta,dim,n,pc):
    pop=pop_curenta.copy()
    for i in range(0,dim-1,2):
        p1=pop[i][0:n]
        p2= pop[i+1][0:n]
        ciclu=CX(p1,p2,n)
        copil1=p1.copy()
        copil2=p2.copy()
        print("Parinte 1:", p1)
        print("Parinte 2:", p2)
        for j in range(n):
            cat,rest=np.divmod(ciclu[j],2)
            if rest==0:
                copil1[j]=p2[j]
                copil2[j] =p1[j]

        print("Copil 1:", copil1)
        print("Copil 2:", copil2)
        pop[i][0:n] = copil1
        pop[i][n] = fitness(copil1)
        pop[i + 1][0:n] = copil2
        pop[i + 1][n] = fitness(copil2)
    return pop

def CX(p1,p2,n):
    ciclu=np.zeros(n)
    index=1
    gata=0
    while not gata:
        poz=np.where(ciclu==0)
        if np.size(poz)!=0: 
            i=poz[0][0]
            a=p1[i]
            ciclu[i]=index
            b=p2[i]
            while a!=b:
                pozitii_b=np.where(p1==b)
                j=pozitii_b[0][0]
                ciclu[j]=index
                b=p2[j]
            index+=1
        else:
            gata=1
    return ciclu'''




'''pop=generare_populatie(15,6)
print(pop)
copii=cicluri(pop,15,6,0.6)
print(copii)'''


'''def elitism(pop_curenta,pop_copii,dim,n):
    copii=np.zeros([dim,n],dtype=int)
    calitati_copii=np.zeros(dim)
    for i in range(dim):
        copii[i][0:n]=pop_copii[i][0:n]
        calitati_copii[i]=pop_copii[i][n]
    calitati_curenta = np.zeros(dim)
    for i in range(dim):
        calitati_curenta[i] = pop_curenta[i][n]
    max_curenta=max(calitati_curenta)
    max_copii= max(calitati_copii)
    if max_curenta>max_copii:
        pozitie_max=[j for j in range(dim) if calitati_curenta[j]==max_curenta]
        poz=pozitie_max[0]
        pozitie_copil=np.random.randint(dim)
        print("Inlocuieste copilul:", copii[pozitie_copil])
        copii[pozitie_copil]=pop_curenta[poz][0:n]
        print("Parinte max:",pop_curenta[poz][0:n])
        calitati_copii[pozitie_copil]=calitati_curenta[poz]
    return copii
'''
'''def sortare(pop,vector_calitati):
    indici=np.argsort(vector_calitati)
    pop_sortata=pop[indici]
    vector_calitati_sortat=vector_calitati[indici]
    return pop_sortata,vector_calitati_sortat'''

'''def genitor(pop_curenta,pop_copii,dim,n,nr_copii):
    pop = np.zeros([dim, n], dtype=int)
    calitati_pop= np.zeros(dim)
    for i in range(dim):
        pop[i][0:n] = pop_curenta[i][0:n]
        calitati_pop[i] = pop_curenta[i][n]
    pop_sortata,calitati_sortat=sortare(pop,calitati_pop)
    pozitii_copil=np.random.randint(0,dim,nr_copii)
    for i in range(nr_copii):
        print("se inlocuieste:", pop_sortata[i])
        print("cu copilul:",pop_copii[pozitii_copil[i]][0:n])
        pop_sortata[i]=pop_copii[pozitii_copil[i]][0:n]
        calitati_sortat[i]=pop_copii[pozitii_copil[i]][n]
    amestec=np.random.permutation(dim)
    pop_urm=pop_sortata[amestec]
    calitati_urm=calitati_sortat[amestec]
    return pop_urm'''

'''def determinism(pop_curenta,pop_copii,dim,n):
    pop = np.zeros([dim, n], dtype=int)
    calitati_pop = np.zeros(dim)
    for i in range(dim):
        pop[i][0:n] = pop_curenta[i][0:n]
        calitati_pop[i] = pop_curenta[i][n]

    pop_c = np.zeros([dim, n], dtype=int)
    calitati_pop_c = np.zeros(dim)
    for i in range(dim):
        pop_c[i][0:n] = pop_copii[i][0:n]
        calitati_pop_c[i] = pop_copii[i][n]

    pop_mare=np.append(pop,pop_c)
    pop_mare.resize(2*dim,n)
    calitati_total=np.append(calitati_pop,calitati_pop_c)
    p,c=sortare(pop_mare, calitati_total)
    print("pop mare:", p)
    pop_noua = [p[i] for i in range(dim,2*dim)]
    calitati_noi=[c[i] for i in range(dim,2*dim)]
    return np.array(pop_noua)'''

'''pop_curenta=generare_populatie(15,6)
pop_copii=generare_populatie(15,6)
print("Populatie curenta:\n",pop_curenta)
print("Populatie copii:\n",pop_copii)
pop_urm=determinism(pop_curenta,pop_copii,15,6)
print(pop_urm)'''