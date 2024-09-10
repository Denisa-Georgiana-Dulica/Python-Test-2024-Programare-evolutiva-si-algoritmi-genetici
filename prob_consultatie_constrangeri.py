'''Fie  f:{1,2,…,350}×{-30,-29,…,10}×{-10,-29,…,10}→R
	f(x_1,x_2,x_3 )=〖-2x1-x2+(x1+x2+x3 )^3
funcţia obiectiv a unei probleme de maxim. Spațiul soluțiilor este reprezentat de mulțimea vectorilor x=(x_1,x_2,x_3 ) din mulţimea
{1,2,…,350}×{-30,-29,…,10}×{-10,-29,…,10} și care îndeplinesc restricția:x_1+x_2+x_3≥0
1)Scrieţi o funcţie Python  pentru generarea aleatoare și evaluarea unei populaţii, pop, cu dimensiunea dim;
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
2)Pentru o probabilitate de mutaţie dată, pm,  scrieţi o funcţie mutaţie pe baza operatorului resetare aleatoare care,
pe baza populaţiei pop obţine o nouă populaţie, cu indivizii eventual mutanţi ai lui pop (calitatea fiecărui individ este memorată
la sfârşitul fiecărei reprezentări cromozomiale).

'''
import numpy as np
def fitness(x):
    scor=0
    scor=-2*x[0]-x[1]+(x[0]+x[1]+x[2])**3
    ok=False
    if x[0]+x[1]+x[2]>=0:
        ok=True
    return scor,ok

def generare_populatie(dim):
    pop=np.zeros([dim,4],dtype=int)
    calitate=np.zeros(dim)
    i=0 #cand am conditii folosesc while si daca se indeplineste cond creste i
    while i<dim:
        pop[i][0]=np.random.randint(1,351)
        pop[i][1] = np.random.randint(-30, 11)
        pop[i][2] = np.random.randint(-10, 11)
        calitate,ok = fitness(pop[i])
        if ok==True:
            pop[i][3]=calitate
            i=i+1 #creste i doar daca se indeplineste conditia
    return pop

def mutatie_resetare_aleatoare(pop,dim,pm):
    popm=pop.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            pozitie=np.random.randint(0,3)
            candidat=popm[i]
            print("Candidat initial:", candidat)
            if pozitie==0:
                candidat[pozitie]=np.random.randint(1,351)
            elif pozitie==1:
                candidat[pozitie] = np.random.randint(-30, 11)
            elif pozitie==2:
                candidat[pozitie] = np.random.randint(-10, 11)
            print("Candidat :", candidat)
            calitate,ok = fitness(candidat[0:3])
            if ok==True:
                popm[i][3]=calitate
                print("Calitate:",popm[i][3])
            else:
                #daca nu e fezabil revin la parintele anterior
                popm[i]=pop[i].copy()
    return popm
pop=generare_populatie(10)
print(pop)
popm=mutatie_resetare_aleatoare(pop,10,0.2)
print(popm)
