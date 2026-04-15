import random
from util.simulate import simulate_route

def random_route(deliveries):
    r = deliveries[:]
    random.shuffle(r)
    return r


def crossover(a, b):
    cut = random.randint(0, len(a))
    child = a[:cut]
    child += [x for x in b if x not in child]
    return child


def mutate(route):
    if len(route) < 2:
        return
    a, b = random.sample(range(len(route)), 2)
    route[a], route[b] = route[b], route[a]


def genetic_algorithm(graph, deliveries, generations=150, pop_size=50):
    population = [random_route(deliveries) for _ in range(pop_size)]

    for _ in range(generations):
        population.sort(key=lambda r: simulate_route(graph, deliveries, r), reverse=True)
        next_gen = population[:10]

        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:20], 2)
            child = crossover(p1, p2)
            if random.random() < 0.3:
                mutate(child)
            next_gen.append(child)

        population = next_gen

    best = max(population, key=lambda r: simulate_route(graph, deliveries, r))
    return simulate_route(graph, deliveries, best)