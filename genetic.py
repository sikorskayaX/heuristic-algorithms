import numpy as np

# The function whose minimum we are seeking
def f(x):
    return 1/5 * x**4 - 11/4 * x**3 + 3 * x**2 + 12 * x

# Genetic algorithm parameters
population_size = 100  # Population size
genes_number = 10      # Number of genes in an individual
mutation_rate = 0.01   # Mutation rate
generations = 10      # Number of generations 
selection_size = 20    # Number of individuals for selection

# Initial population initialization
population = np.random.uniform(0, 10, (population_size, genes_number))

# Function to evaluate the fitness of an individual
def fitness(individual):
    return f(individual.mean())

# Genetic algorithm
for generation in range(generations):
    # Evaluate the fitness of each individual
    fitness_values = np.array([fitness(ind) for ind in population])
    # Selection of the best individuals
    best_indices = fitness_values.argsort()[:selection_size]
    selected = population[best_indices]
    
    # Crossover of individuals
    offspring = []
    for i in range(int(population_size / 2)):
        parents = selected[np.random.choice(selection_size, 2, replace=False)]
        cross_point = np.random.randint(1, genes_number)
        child1 = np.concatenate((parents[0][:cross_point], parents[1][cross_point:])) 
        child2 = np.concatenate((parents[1][:cross_point], parents[0][cross_point:]))
        offspring.extend([child1, child2])
    population = np.array(offspring)
    
    # Mutation
    mutation_indices = np.random.choice([True, False], size=population.shape, p=[mutation_rate, 1 - mutation_rate])
    population[mutation_indices] = np.random.uniform(0, 10, size=population[mutation_indices].shape)
    
    # Print the best individual and its fitness
    best_individual = population[fitness_values.argmin()]
    print(f"Generation {generation}: x = {best_individual.mean():.4f}, f(x) = {fitness(best_individual):.4f}")

# Print the best individual from the last generation
best_individual = population[fitness_values.argmin()]
print("Best individual: ", f"x = {best_individual.mean():.4f}, f(x) = {fitness(best_individual):.4f}")
