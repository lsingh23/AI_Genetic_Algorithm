import random as r
from numpy import *

NO_OF_QUEENS = 8              #Number of Queens
POPULATION_SIZE = 20          #Size of Population


# check number of diagonal conflicts for chromosome
def diag_conflict(chromosome):
    n = len(chromosome)

    primary_diagonal = [0] * (2 * n)
    secondary_diagonal = [0] * (2 * n)

    for i in range(n):
        primary_diagonal[chromosome[i] + i] += 1
        secondary_diagonal[n - chromosome[i] + i] += 1

    conflicts = 0

    for i in range(2*n):
        # Formula used :  N * (N-1) / 2
        conflicts += (primary_diagonal[i] * (primary_diagonal[i]-1)) / 2
        conflicts += (secondary_diagonal[i] * (secondary_diagonal[i]-1)) / 2
    return int(conflicts)

# check no. of horizontal conflicts in chromosome
def horizontal_conflict(chromosome):
    horizontal_collisions = 0
    for queen in chromosome:
        horizontal_collisions += chromosome.count(queen) - 1
    return int(horizontal_collisions / 2)

# check if a value exists in array
def notInArray(arr, x): 
  for element in arr: 
    if element == x: return False 
  return True 
  
# perform mutation for given chromosome
def mutation(chromosome):
    arr = [] # this will contain the indices of the duplicate values
    arr2 = [] # this will contain all the values not present in the chromosome 
    indexArray = [] 
    
    c1 = 0
    index = None 
    
    #for loop to calculate indices of duplicate values 
    for queen in chromosome: 
      c2 = 0 
    
      for duplicate in chromosome:
        if queen == duplicate and c1 != c2 and notInArray(indexArray, c1): 
          index = chromosome.index(duplicate)
          arr.append(c2)
          indexArray.append(c2)
        c2 += 1 
      c1 += 1       
    
    #for loop to find values not present in the chromosome 
    n = [1, 2, 3, 4, 5, 6, 7, 8] 
    for element in n: 
      result = False 
      for queen in chromosome: 
        if queen == element: result = True 
      if result == False: arr2.append(element) 
    
    #changing the duplicate values to the ones not present 
    i = 0   
    for element in arr: 
      chromosome[element] = arr2[i]  
      i += 1 
    
    return chromosome 
    
# calculat fitness of chromosome
def fitness(chromosome):
    horizontal_conflicts = horizontal_conflict(chromosome)
    diagonal_conflicts = diag_conflict(chromosome)
    return int(maxFitness - (horizontal_conflicts + diagonal_conflicts))

# generate a random chromosome
def random_chromosome():
    return [random.randint(1, NO_OF_QUEENS) for _ in range(NO_OF_QUEENS)]

# calculate Probabilities for population
def calculateProbabilities(population):
    return [(fitness(chromosome) / maxFitness) for chromosome in population]

# choose a Parent based on probabilities
def chooseParent(population, probabilities):
    return r.choices(population, weights=probabilities, k=1)
    
#do crossover for two chromosomes
def crossover(x, y):
    n = len(x)
    c = r.randint(0, n - 1)
    return x[0:c] + y[c:n], y[0:c] + x[c:n]
  
#genetic algorithm for population
def genetic_algorithm(population):
    new_population = []
    probabilities = calculateProbabilities(population)
    for i in range(len(population)):
        # parent 1
        x = chooseParent(population, probabilities) 
        print("parent 1 : " + str(x))
        # parent 2
        y = chooseParent(population, probabilities) 
        print("parent 2 : " + str(y))
        childs = crossover(x[0], y[0]) 
        for child in childs:
             print ("Before mutation: " + str(child)) 
             childNew = mutation(child)
             print("After mutation: " + str(childNew))
             new_population.append(childNew)
        if fitness(child) == maxFitness: break
    return new_population


################ testing code ##############

maxFitness = (NO_OF_QUEENS * (NO_OF_QUEENS - 1)) / 2  #max fitness

population = [random_chromosome() for _ in range(POPULATION_SIZE)] # generate population

for chromosome in population:
    print("fitness of chromosome:  " + str(chromosome) + " is : " + str(fitness(chromosome)))

generation = 1

# produce new generations until we find a chromosome with max fitness value
while not maxFitness in [fitness(chromosome) for chromosome in population]:
        print("Generation : "+ str(generation))
        population = genetic_algorithm(population)
        print("")
        print("Maximum Fitness: " + str(max([fitness(n) for n in population])))
        generation += 1

# solution
print("Solved in Generation: " + str(generation-1))
for chromosome in population:
    if fitness(chromosome) == maxFitness:
        print("")
        print("Solution ===>")
        print(chromosome)


