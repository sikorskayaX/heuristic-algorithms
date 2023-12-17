import numpy as np

# Функция, минимум которой мы ищем
def f(x):
    return 1/5 * x**4 - 11/4 * x**3 + 3 * x**2 + 12 * x

# Параметры генетического алгоритма
population_size = 100  # Размер популяции
genes_number = 10      # Количество генов в индивиде
mutation_rate = 0.01   # Вероятность мутации
generations = 20      # Количество поколений
selection_size = 20    # Количество особей для селекции

# Инициализация начальной популяции
population = np.random.uniform(0, 10, (population_size, genes_number))

# Функция для оценки приспособленности особи
def fitness(individual):
    return f(individual.mean())

# Генетический алгоритм
for generation in range(generations):
    # Оценка приспособленности каждой особи
    fitness_values = np.array([fitness(ind) for ind in population])
    
    # Селекция лучших особей
    best_indices = fitness_values.argsort()[:selection_size]
    selected = population[best_indices]
    
    # Скрещивание (кроссовер) особей
    offspring = []
    for _ in range(int(population_size / 2)):
        parents = selected[np.random.choice(selection_size, 2, replace=False)]
        cross_point = np.random.randint(1, genes_number)
        child1 = np.concatenate((parents[0][:cross_point], parents[1][cross_point:]))
        child2 = np.concatenate((parents[1][:cross_point], parents[0][cross_point:]))
        offspring.extend([child1, child2])
    population = np.array(offspring)
    
    # Мутация
    mutation_indices = np.random.choice([True, False], size=population.shape, p=[mutation_rate, 1 - mutation_rate])
    population[mutation_indices] = np.random.uniform(0, 10, size=population[mutation_indices].shape)
    
    # Выводим лучшую особь и ее приспособленность
    best_individual = population[fitness_values.argmin()]
    print(f"Generation {generation}: Best fitness = {fitness(best_individual):.4f}, x = {best_individual.mean():.4f}")

# Выводим лучшую особь из последнего поколения
best_individual = population[fitness_values.argmin()]
print(f"Best individual: x = {best_individual.mean():.4f}, f(x) = {fitness(best_individual):.4f}")
