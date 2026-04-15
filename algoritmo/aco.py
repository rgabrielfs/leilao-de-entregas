import random
from util.simulate import simulate_route

def aco(graph, deliveries, iterations=80, ants=30):
    nodes = list(set(['A'] + [d.destination for d in deliveries]))

    pheromone = {(i, j): 1.0 for i in nodes for j in nodes if i != j}

    def choose(current, remaining):
        weights = []
        for d in remaining:
            tau = pheromone.get((current, d.destination), 1.0)
            eta = d.bonus / (graph.cost(current, d.destination) + 1)
            weights.append((d, tau * eta))

        total = sum(w for _, w in weights)
        r = random.random() * total

        s = 0
        for d, w in weights:
            s += w
            if s >= r:
                return d

        return remaining[0]

    best = 0

    for _ in range(iterations):
        solutions = []

        for _ in range(ants):
            remaining = deliveries[:]
            current = 'A'
            route = []

            while remaining:
                d = choose(current, remaining)
                route.append(d)
                remaining.remove(d)
                current = d.destination

            score = simulate_route(graph, deliveries, route)
            solutions.append((route, score))
            best = max(best, score)

        for k in pheromone:
            pheromone[k] *= 0.85

        for route, score in solutions:
            for i in range(len(route) - 1):
                a = route[i].destination
                b = route[i + 1].destination
                pheromone[(a, b)] += score / 100

    return best