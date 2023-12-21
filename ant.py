import numpy as np

# Distance matrix
distance_matrix = np.array([
    [np.inf, 38, 74, 59, 45],
    [38, np.inf, 46, 61, 72],
    [74, 46, np.inf, 49, 85],
    [59, 61, 49, np.inf, 42],
    [45, 72, 85, 42, np.inf]
])

# Ant colony algorithm parameters
num_cities = distance_matrix.shape[0]
num_ants = 20
num_iterations = 100
decay = 0.5
alpha = 1.0  # Influence of pheromone
beta = 2.0   #  Influence of visibility (1/distance)

# Pheromone initialization
pheromone = np.ones((num_cities, num_cities)) / num_cities
visibility = 1 / (distance_matrix + 1e-10)  # Add a small constant to avoid division by zero
# Pheromone update function
def update_pheromone(pheromone, ants_paths, ants_lengths):
    pheromone *= decay  # Pheromone decrease
    for path, length in zip(ants_paths, ants_lengths):
        for i in range(num_cities - 1):
            pheromone[path[i], path[i+1]] += 1.0 / length
        pheromone[path[-1], path[0]] += 1.0 / length  # Return to starting city return pheromone
    return pheromone

# Ant colony method
best_length = np.inf
best_path = None
for iteration in range(num_iterations):
    ants_paths = []
    ants_lengths = []
    for ant in range(num_ants):
        path = [np.random.randint(num_cities)]  # Starting city for ant
        while len(path) < num_cities:
            current_city = path[-1]
            probabilities = pheromone[current_city] ** alpha * visibility[current_city] ** beta
            probabilities[path] = 0  # Already visited cities are excluded
            next_city = np.random.choice(num_cities, p=probabilities / probabilities.sum())
            path.append(next_city)
        length = sum(distance_matrix[path[i], path[i+1]] for i in range(-1, num_cities - 1))
        ants_paths.append(path)
        ants_lengths.append(length)
        if length < best_length:
            best_length = length
            best_path = path
    pheromone = update_pheromone(pheromone, ants_paths, ants_lengths)

print("Best path: ", best_path)
print("Length of best path: ", best_length)
