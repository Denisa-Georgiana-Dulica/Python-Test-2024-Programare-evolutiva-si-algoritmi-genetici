import numpy as np
'''Fie 𝑓:{1,2,…,1500}×{−1,0,,…,2500}→ℝ,𝑓(𝑥,𝑦)=𝑦∗(𝑠𝑖𝑛(𝑥−2))^2
funcţia obiectiv a unei probleme de maxim. Fiecărui fenotip (𝑥,𝑦)∈{1,2,…,1500}×{−1,0,…,2500}
îi corespunde un genotip şir binar obţinut prin reprezentarea în bază 2 a fiecărei componente a fenotipului.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; 
calitatea fiecărui individ este memorată la sfârşitul fiecărei reprezentări cromozomiale;
b.Pentru o probabilitate de recombinare dată, pc, scrieţi o funcţie de recombinare utilizând operatorul de încrucişare 
multi-punct pentru 3 puncte de încrucişare care, pe baza populaţiei pop obţine o nouă populaţie, popc. 
Populaţia rezultată are tot dim indivizi (este utilizată şi recombinarea asexuată şi calitatea fiecărui individ este memorată la sfârşitul 
fiecărei reprezentări cromozomiale).
'''
# sir_binar = bin(n)[2:] #n se transforma intr-un string, sir de biti 01 ( '1010' )
# sir_binar_final = sir_binar.zfill(m)  # o sa umplu acel string cu 0 pana la nr de biti m (m=7 '0001010')
# string-> lista x=np.zeros(m) x[i] = int(sir_binar_final[i])
# bin(x) are 11 biți (1024=2^10<1500<2^11=2048)
# bin(y+1) are 12 biți (2048=2^11<2501<2^12=4096)
#fiecărui fenotip (𝑥,𝑦)∈{1,2,…,1500}×{−1,0,…,2500} îi corespunde un genotip şir binar --> un individ o sa aiba 11 biti+ 12 biti pentru ca un individ este [x,y]
import numpy as np

def baza_10_baza_2(candidat,nr_biti):
    sir_binar=bin(candidat)[2:]
    sir_binar_final=sir_binar.zfill(nr_biti)
    vector_binar=np.zeros(nr_biti,dtype=int)
    for i in range(nr_biti):
        vector_binar[i]=int(sir_binar_final[i])
    return list(vector_binar)

def baza_2_baza_10(vector_binar,nr_biti):
    sir_biti=''
    for i in range(nr_biti):
        sir_biti+=str(vector_binar[i])
    numar=int(sir_biti,2)
    return numar

def fitness(candidat):
    x1=baza_2_baza_10(candidat[0:11],11)
    x2=baza_2_baza_10(candidat[11:23],12)
    scor = x2 * ((np.sin(x1 - 2)) ** 2)
    return scor

#un individ are 23 biti - reprezentarea binara a numerelor din {1,...,1500} concatenata cu
# reprezentarea binara a numerelor din {0,...,2501}
def generare_populatie(dim):
    pop=np.zeros([dim,24],dtype=int)
    for i in range(dim):
        x1=np.random.randint(0,1501)
        x2 = np.random.randint(0, 2502)
        print("Componentele in baza 10 (fenotipul):", x1, x2)

        individ=baza_10_baza_2(x1,11)+baza_10_baza_2(x2,12) #trebuie sa imi dea list pentru ca altfel nu le pot concatena
        print("Reprezentarea genotipului", individ)

        pop[i][0:23]=individ
        pop[i][23]=fitness(individ)
        print("Fitness:",  pop[i][23])
    return pop

def recombinare_3pct_multipunct(pop,dim,pc,n): #n=23
    populatie=pop.copy()
    for i in range(0,dim-1,2):
        p1=populatie[i][0:n]
        p2 = populatie[i+1][0:n]
        r=np.random.uniform(0,1)
        if r<=pc:
            m=np.random.randint(0,n-2) #am pus m ca sa nu se incurce cu i de sus
            j=np.random.randint(m+1,n-1)
            k=np.random.randint(j+1,n)

            copil1=p1.copy() #in copil1 copiez parinte 1
            copil2=p2.copy() #in copil2 copiez parinte 2

            print("parinte 1:", p1)
            print("parinte 2:", p2)

            copil1[j:k+1]=p2[j:k+1]
            copil2[j:k + 1] = p1[j:k + 1]

            print("copil 1:  ",copil1)
            print("copil 2:  ", copil2)

            populatie[i][0:n]=copil1
            populatie[i][n]=fitness(copil1)
            print("Fitness copil 1:", populatie[i][n])

            populatie[i+1][0:n] = copil2
            populatie[i+1][n] = fitness(copil2)
            print("Fitness copil 2:", populatie[i+1][n])
    return pop

vector=baza_10_baza_2(1500,11)
vector2=baza_10_baza_2(2000,12)
print(vector)
print(vector2)
numar=baza_2_baza_10(vector,11)
print(numar)
candidat=np.array([1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0,0,1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0]) # 1500+2000
scor=fitness(candidat)
print(scor)

pop=generare_populatie(10)
print(pop)
populatie_copii=recombinare_3pct_multipunct(pop,10,0.6,23)
print(populatie_copii)









