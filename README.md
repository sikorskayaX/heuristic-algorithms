# Heuristic algorithms

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## Install 
```bash
# pip

$ python -m pip install -U pip
$ pip install numpy


# git

$ git clone https://github.com/sikorskayaX/heuristic-algorithms.git
```

## genetic algorithm 🧬

This code implements a <b> genetic algorithm </b>to find the minimum of the function f(x).

The steps that the code performs:
- Initializing the population: An initial population is created from population size individuals, each
of which is represented by an array of genes number genes. Genes are initialized with random
numbers in the range from 0 to 10.
- Fitness assessment: For each individual, the average value of its genes is calculated, and this
average value is used to calculate the value of the function f(x). Fitness of the individual
It is defined as the value of the function f(x) for this average value.
- Selection: The selection size of the best individuals (with the lowest
values of the function f(x)) is selected from the current population.
- Interbreeding: Selected individuals are interbred to create a new generation. For each
pair of parents, a crossing point is randomly selected, and
the corresponding parts of their genes are exchanged to create two offspring.
- Mutation: With some low probability of mutation rate, each gene in the population can
be randomly changed - this introduces new variations into the population.
- Repeat: Steps 2-5 are repeated for a given number of generations.

<b> Output of the result: </b> The smallest value of x and the minimum of the function at the minimum point

## example of working 
Input params:

```bash
# The function whose minimum we are seeking
def f(x):
    return 1/5 * x**4 - 11/4 * x**3 + 3 * x**2 + 12 * x

# Genetic algorithm parameters
population_size = 100  # Population size
genes_number = 10      # Number of genes in an individual
mutation_rate = 0.01   # Mutation rate
generations = 10      # Number of generations 
selection_size = 20    # Number of individuals for selection
```

Output result :
```bash
Generation 0: x = 6.4620, f(x) = -190.4947
Generation 1: x = 7.0549, f(x) = -236.1998
Generation 2: x = 8.0801, f(x) = -305.3853
Generation 3: x = 8.4314, f(x) = -323.1256
Generation 4: x = 8.8041, f(x) = -336.8545
Generation 5: x = 8.9628, f(x) = -340.8062
Generation 6: x = 9.0758, f(x) = -342.8424
Generation 7: x = 9.3031, f(x) = -344.8144
Generation 8: x = 9.2684, f(x) = -344.7065
Generation 9: x = 9.3363, f(x) = -344.8498
Best individual:  x = 9.3363, f(x) = -344.8498
```

## ant algorithm 🐜

This code implements the <b>ant colony algorithm</b> to solve the traveling salesman problem, which
is to find the shortest possible path through a given set of cities,
returning to the original city.
The ant colony algorithm uses the following variables:
- Pheromone: A substance left by ants along the path that can be
detected by other ants. The pathway with a large amount of pheromone is considered more
preferable.
- Visibility: The inverse of the distance between cities. The closer the city is, the higher it is
visibility and the more likely it is that the ant will go to this city.
Alpha: A parameter that determines the effect of a pheromone on the probability of choosing a path.
Beta: A parameter that determines the effect of visibility on the probability of choosing a path.
- Evaporation (decay): A pheromone evaporation coefficient that reduces the amount
of pheromone in all pathways after each iteration to avoid premature convergence to
a local optimum.
The algorithm works as follows:
- Initialization: A pheromone matrix is created, where each element represents a number of-
The pheromone is on the way between the two cities. Initially, all values are set to equal
1 / num cities.
- Building Solutions: Each ant builds its own path, starting from a random city. The
ant then consistently chooses the next city to visit based on probabilities
that depend on the amount of pheromone and visibility. The visited cities are excluded from
further consideration.
- Pheromone Renewal: After all the ants have built their paths, the amount
of pheromone on the paths decreases by the evaporation coefficient. Then it is added to each path
a new pheromone inversely proportional to the length of the path that the ant has traveled.
- Repetition: Steps 2 and 3 are repeated for a specified number of iterations num iterations.

<b> Output of the result: </b> The shortest path and its length, found during the entire operation
of the algorithm, are output.
The code uses np.inf to indicate infinity in the distance matrix in order to
prevent the choice of a path from the city to it. Adding a small constant 1e-10 to
the distance matrix when calculating visibility prevents division by zero.

## example of working 
Input params:

```bash
# Distance matrix
distance_matrix = np.array([
    [np.inf, 38, 74, 59, 45],
    [38, np.inf, 46, 61, 72],
    [74, 46, np.inf, 49, 85],
    [59, 61, 49, np.inf, 42],
    [45, 72, 85, 42, np.inf]
])

# Starting city for ant
path = [np.random.randint(num_cities)]  
```

Output result :
```bash
Length of best path:  220.0
```
