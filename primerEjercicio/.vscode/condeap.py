
import random

import numpy
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
ind_size=4

df=pd.read_csv(open('datos.csv'))

print(" ")
df.rename(index={0:'Monoblock',1:'Ingenieria',2:'Derecho',3:'Cota Cota'}, inplace=True)
df.head()
print(df)
distances=df.to_numpy()

print("\nDistancia\n%s"% distances)


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(ind_size), ind_size)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def EVALUATE(individual):
    print("Que es individual", individual)
    for it in individual:
      if(it == 0 ):
        print('Monoblock')
      if(it == 1 ):
        print('Ingenieria')
      if(it == 2 ):
        print('Derecho')
      if(it == 3 ):
        print('Cota Cota')    
      
    summation = 0
    min = 9999
    start = individual[0]
    for i in range(1, len(individual)+1):
        end = individual[i]
        summation += distances[start][end]
        #print("indice=",str(i),"[",str(start),"][",str(end),"]=suma:",summation) 
        if(min>summation):
          min = summation
        start = end
         
    return summation



toolbox.register("evaluate", EVALUATE)
print(min)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0/ind_size)
toolbox.register("select", tools.selTournament, tournsize=3)


def main(seed=0):   
    random.seed(seed)
    pop = toolbox.population(n=30)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, stats=stats,halloffame=hof, verbose=False)
    # print(pop)
    # print(stats)
    # print(hof)
    return pop, stats, hof

if __name__ == "__main__":
    main()