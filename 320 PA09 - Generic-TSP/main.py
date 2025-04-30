import random
from functools import partial
from init_pop import *
from load_dist import *
from util import *


def order_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    offspring = [None] * size

    for i in range(start, end):
        offspring[i] = parent1[i]

    current_pos = 0
    for i in range(size):
        if offspring[i] is None:
            while parent2[current_pos] in offspring:
                current_pos += 1
            offspring[i] = parent2[current_pos]

    return tuple(offspring)


def mutate(path):
    path = list(path)
    i, j = random.sample(range(len(path)), 2)
    path[i], path[j] = path[j], path[i]
    return tuple(path)


def ga_tsp(initial_population, distances, generations):
    if initial_population is None or not isinstance(initial_population, list):
        return None
    if distances is None or not isinstance(distances, (dict, str)):
        return None
    if generations is None or not isinstance(generations, int) or generations <= 0:
        return None

    if len(initial_population) == 0:
        return None

    valid_initial_population = [
        path for path in initial_population if cost(path, distances) is not None
    ]

    if valid_initial_population:
        best_initial_path = min(
            valid_initial_population, key=partial(cost, distances=distances)
        )

    valid_population = [
        path for path in initial_population
        if valid_path(path) and cost(path, distances) is not None
    ]

    if not valid_population:
        return None

    for generation in range(generations):
        parent1 = random.choice(valid_population)
        parent2 = random.choice(valid_population)
        child = order_crossover(parent1, parent2)

        if random.random() < 0.1:
            child = mutate(child)
        if valid_path(child) and cost(child, distances) is not None:
            valid_population.append(child)

        valid_population = [
            path for path in valid_population
            if valid_path(path) and cost(path, distances) is not None
        ]
        valid_population = sorted(
            valid_population, key=partial(cost, distances=distances)
        )
        valid_population = valid_population[:len(initial_population)]

    best_path_result = best_path(valid_population, distances)

    return best_path_result
