#f:{1,2,…,1500}×{-1,0,,…,2500}×{10,11,…,250}×{10,11,…,250}→R,f(x,y,z,t)=〖y*(sin(x-2))〗^2+z+t

import numpy as np
#RECOMBINARE MULTIPUNCT IN 3 PUNCTE PENTRU NR INTREGI
def fitness(candidat):
    scor=0
    scor=candidat[1]*(np.sin(candidat[0]-2))**2+candidat[2]+candidat[3]
    return scor

def generare_populatie(dim):
    pop=np.zeros([dim,5],dtype =int)
    for i in range(dim):
        pop[i][0]=np.random.randint(0,1501)
        pop[i][1] = np.random.randint(-1, 2501)
        pop[i][2] = np.random.randint(10, 250)
        pop[i][3] = np.random.randint(10, 250)
        pop[i][4]=fitness(pop[i][0:4])
    return pop

def recombinare_multipunct_nr_intregi(pop,dim,pc,n): #n=4
    popc=pop.copy()
    for i in range(0,dim-1,2):
        p1=popc[i][0:n]
        p2=popc[i+1][0:n]
        r=np.random.uniform(0,1)
        print(r)
        if r<=pc:
            m=np.random.randint(0,n-2)
            j=np.random.randint(m+1,n-1)
            k=np.random.randint(j+1,n)

            print("parinte 1:", p1)
            print("parinte 2:", p2)

            copil1=p1.copy()
            copil2=p2.copy()

            copil1[j:k+1]=p2[j:k+1]
            copil2[j:k+1]=p1[j:k+1]

            print("copil 1:  ", copil1)
            print("copil 2:  ", copil2)

            popc[i][0:n]=copil1
            popc[i+1][0:n] = copil2

            popc[i][n]=fitness(copil1)
            print("Fitness copil 1:", popc[i][n])
            popc[i+1][n] = fitness(copil2)
            print("Fitness copil 2:", popc[i + 1][n])
    return popc


pop=generare_populatie(10)
print(pop)
popc=recombinare_multipunct_nr_intregi(pop,10,0.6,4)
print(popc)
