import numpy as np

# Матрица расстояний
distance_matrix = np.array([
    [np.inf, 38, 74, 59, 45],
    [38, np.inf, 46, 61, 72],
    [74, 46, np.inf, 49, 85],
    [59, 61, 49, np.inf, 42],
    [45, 72, 85, 42, np.inf]
])

# Параметры алгоритма муравьиных колоний
num_cities = distance_matrix.shape[0]
num_ants = 20
num_iterations = 100
decay = 0.5
alpha = 1.0  # Влияние феромона
beta = 2.0   # Влияние видимости (1/расстояние)

# Инициализация феромонов
pheromone = np.ones((num_cities, num_cities)) / num_cities
visibility = 1 / (distance_matrix + 1e-10)  # Добавляем небольшую константу, чтобы избежать деления на ноль

# Функция для обновления феромонов
def update_pheromone(pheromone, ants_paths, ants_lengths):
    pheromone *= decay  # Уменьшение феромона
    for path, length in zip(ants_paths, ants_lengths):
        for i in range(num_cities - 1):
            pheromone[path[i], path[i+1]] += 1.0 / length
        pheromone[path[-1], path[0]] += 1.0 / length  # Возвращение в начальный город
    return pheromone

# Метод муравьиных колоний
best_length = np.inf
best_path = None
for iteration in range(num_iterations):
    ants_paths = []
    ants_lengths = []
    for ant in range(num_ants):
        path = [np.random.randint(num_cities)]  # Начальный город для муравья
        while len(path) < num_cities:
            current_city = path[-1]
            probabilities = pheromone[current_city] ** alpha * visibility[current_city] ** beta
            probabilities[path] = 0  # Уже посещенные города исключаются
            next_city = np.random.choice(num_cities, p=probabilities / probabilities.sum())
            path.append(next_city)
        length = sum(distance_matrix[path[i], path[i+1]] for i in range(-1, num_cities - 1))
        ants_paths.append(path)
        ants_lengths.append(length)
        if length < best_length:
            best_length = length
            best_path = path
    pheromone = update_pheromone(pheromone, ants_paths, ants_lengths)

print("Длина лучшего пути: ", best_length)
