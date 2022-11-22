# AI Genetic Algorithm
8-queen-problem using ai genetic algorithm



Tester starts with calculating the maxFitness for the 8 queen 
problem using the formula : 
(NO_OF_QUEENS * (NO_OF_QUEENS - 1)) / 2

Then generate a population of the size defined. 
Next, calculate the fitness of these chromosomes and display it in order of chromosome index,
and then start the genetic loop starting with generation 1.
Run this loop until a chromosome with maxFitness is found in the population.
The genetic_alogrithm method takes the population and returns a new population by doing 
crossovers and mutations.

Starting with calculating the fitness probabilities for each chromosome in population and then 
choose x and y chromosome based on best percentage probabilities. Then after crossover do the 
mutation and remove the duplicate values from the chromosome.

We can repeat this procedure until we find a chromosome with a fitness value of 28 and return that as 
a solution
