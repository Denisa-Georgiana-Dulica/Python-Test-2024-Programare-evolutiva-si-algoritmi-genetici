''''Fie 𝑓:𝒫(𝑛)→ℕ 𝑝𝜖𝒫(𝑛),𝑓(𝑝)=|{(𝑖,𝑗)𝑖<𝑗,𝑝(𝑖)=𝑗 ş𝑖 𝑝(𝑗)=𝑖⁄}| funcţia obiectiv a unei probleme de maxim, unde 𝒫(𝑛) desemnează mulţimea permutărilor de n elemente.
a.Scrieţi o funcţie Python pentru generarea aleatoare a unei populaţii, pop, cu dimensiunea dim; calitatea fiecărui individ este memorată la sfârşitul
fiecărei reprezentări cromozomiale;
b.Pentru o probabilitate de mutaţie dată, pm, scrieţi o funcţie de mutaţie utilizând operatorul de mutaţie prin interschimbare care, pe baza populaţiei pop
obţine o nouă populaţie, popm. Populaţia rezultată are tot dim indivizi.'''
import numpy as np
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
    for i in range(dim):
        candidat=np.random.permutation(n)
        pop[i][0:n]=candidat
        pop[i][n]=fitness(candidat)
    return pop

def mutatie_interschimbare(pop,dim,pm):
    popm=pop.copy()
    interval=np.random.randint(0,len(pop[0])-1,2)
    if interval[0]==interval[1]:
        interval = np.random.randint(0, len(pop[0]) - 1, 2)
    interval_min=min(interval)
    interval_max = max(interval)
    for i in range(dim):
        candidat=popm[i]
        r=np.random.uniform(0,1)
        if r<=pm:
            print("Candidat initial:", candidat)
            temp=candidat[interval_min]
            candidat[interval_min]=candidat[interval_max]
            candidat[interval_max]=temp
            print("Mutatie:", candidat)
            calitate_noua=fitness(candidat[0:(len(pop[0])-1)])
            candidat[len(pop[0])-1]= calitate_noua
            print("Calitate noua:", candidat[len(pop[0])-1])
    return popm
scor = fitness(t)
print(scor)
populatie = generare_populatie(20, 6)
print(populatie)
popm = mutatie_interschimbare(populatie, 20, 0.1)
print(popm)


