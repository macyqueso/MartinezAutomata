#SOLVING THE KNAPSACK PROBLEM

import random

items = [("laptop",3,4),("phone",1,3),("book",2,1),("tablet",2,3),("charger",1,2)]
MAX_WEIGHT = 5

def fitness_knapsack(chromosome):
    weight = sum(items[i][1] for i in range(len(chromosome)) if chromosome[i])
    value  = sum(items[i][2] for i in range(len(chromosome)) if chromosome[i])
    return value if weight <= MAX_WEIGHT else 0

def genetic_knapsack():
    n = len(items)
    population = [[random.randint(0,1) for _ in range(n)] for _ in range(30)]

    for _ in range(200):
        population.sort(key=fitness_knapsack, reverse=True)
        survivors = population[:15]

        offspring = []
        for _ in range(15):
            p1, p2 = random.sample(survivors, 2)
            cut = random.randint(1, n-1)
            child = p1[:cut] + p2[cut:]  # Single-point crossover
            # Mutation
            if random.random() < 0.1:
                idx = random.randint(0, n-1)
                child[idx] = 1 - child[idx]
            offspring.append(child)

        population = survivors + offspring

    best = max(population, key=fitness_knapsack)
    chosen = [items[i][0] for i in range(n) if best[i]]
    weight = sum(items[i][1] for i in range(n) if best[i])
    value  = sum(items[i][2] for i in range(n) if best[i])
    print(f"Items: {chosen}\nWeight: {weight}, Value: {value}")

genetic_knapsack()