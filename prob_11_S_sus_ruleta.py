'''11.
Fie 𝑓:{1,2,…,500}→ℝ,𝑓(𝑥)=(𝑠𝑖𝑛(𝑥−2))^2 funcţia obiectiv a unei probleme de maxim.
Fiecărui fenotip 𝑥 ={1, 2,.. 500} îi corespunde un genotip şir binar obţinut prin reprezentarea standard în bază 2 a lui x.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b.Scrieţi o funcţie Python care, pentru populaţia generată pop obţine o populaţie de părinţi prin aplicarea selecţiei de tip ruletă cu
distribuţia de probabilitate FPS cu sigma-scalare.'''
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
    pop=np.zeros([dim,nr_biti+1],dtype=int)
    for i in range(dim):
        x=np.random.randint(1,501)
        sir_binar=baza10_baza2(x,nr_biti)
        pop[i][0:nr_biti]=sir_binar
        pop[i][nr_biti]=fitness(sir_binar,nr_biti)
    return pop
#fps+sigma scalare+ruleta
def sigma_scalare(pop,dim,nr_biti):
    vector_calitati_noi = np.zeros(dim)
    vector_calitati=np.zeros(dim)
    for i in range(dim):
        vector_calitati[i]=pop[i][nr_biti]
    med=np.mean(vector_calitati)
    var=np.std(vector_calitati)
    for i in range(dim):
        vector_calitati_noi[i]=max(0,vector_calitati[i]-(med-2*var))
    if np.sum(vector_calitati_noi)==0:
        dis=fps(vector_calitati,dim)
    else:
        dis = fps(vector_calitati_noi, dim)
    return dis

def fps(vector_calitati,dim):
    fps=np.zeros(dim)
    suma=np.sum(vector_calitati)
    for i in range(dim):
        fps[i]=vector_calitati[i]/suma
    dis=fps.copy()
    for i in range(1,dim):
        dis[i]=dis[i-1]+fps[i]
    return dis
'''def ruleta(pop,dim,nr_biti):
    parinti=pop.copy()
    distributia_cumulata=sigma_scalare(pop,dim,nr_biti)
    for i in range(dim):
        r=np.random.uniform(0,1)
        poz=[j for j in range(dim) if distributia_cumulata[j]>=r]
        pozitie_min=min(poz)
        parinti[i][0:nr_biti]=pop[pozitie_min][0:nr_biti]
        parinti[i][nr_biti]=fitness(pop[pozitie_min][0:nr_biti],nr_biti)
    return parinti
'''
def SUS(pop,dim,nr_biti):
    parinti=pop.copy()
    distributie_cumulata=sigma_scalare(pop,dim,nr_biti)
    i=0 #pentru a indexa parintii
    j=0 #pentru distributie
    r=np.random.uniform(0,1/dim)
    while i<dim:
        #iau prima distributie si generez r (pe care il cresc de fiecare data) pana gasesc unul care e mai mare decat dis
        while r<=distributie_cumulata[j]:
            parinti[i][0:nr_biti]=pop[i][0:nr_biti]
            parinti[i][nr_biti]=pop[i][nr_biti]
            r+=1/dim
            #cresc i pentru ca am indexul de la parinti
            i=i+1
        #daca r e > decat dis --> ma duc la valoarea urmatoare a distributiei
        j=j+1
    return parinti


nr=baza10_baza2(500,9)
print(nr)
numar_10=baza2_baza10(nr,9)
print(numar_10)
calitate=fitness(nr,9)
print(calitate)

pop=generare_populatie(10,9)
print(pop)
parinti=SUS(pop,10,9)
print("Parinti:",parinti)