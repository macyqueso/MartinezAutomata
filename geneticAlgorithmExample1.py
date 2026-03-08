#MAXIMIZE A MATHEMATICAL FUNCTION

import random

def fitness(x):
    return -(x**2) + 10*x + 5  # Max at x=5

def genetic_algorithm():
    population = [random.uniform(0, 10) for _ in range(20)]

    for generation in range(100):
        # Evaluate and sort by fitness
        population.sort(key=fitness, reverse=True)

        # Keep top 50% (selection)
        survivors = population[:10]

        # Crossover: create offspring from pairs
        offspring = []
        for i in range(10):
            p1, p2 = random.sample(survivors, 2)
            child = (p1 + p2) / 2  # Midpoint crossover
            offspring.append(child)

        # Mutation: small random tweak
        offspring = [x + random.uniform(-0.5, 0.5) for x in offspring]

        population = survivors + offspring

    best = max(population, key=fitness)
    print(f"Best x = {best:.4f}, f(x) = {fitness(best):.4f}")

genetic_algorithm()