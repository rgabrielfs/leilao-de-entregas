import time

from models.graph import Graph
from models.entregas import Delivery

from algoritmo.heuristica import astar
from algoritmo.ag import genetic_algorithm
from algoritmo.aco import aco

import matplotlib.pyplot as plt

def run_all():
    graph = Graph({
        'A': {'B':5,'C':0,'D':2},
        'B': {'A':5,'C':3,'D':0},
        'C': {'A':0,'B':3,'D':8},
        'D': {'A':2,'B':0,'C':8}
    })

    deliveries = [
        Delivery('B', 0, 1),
        Delivery('C', 5, 10),
        Delivery('D', 10, 8)
    ]

    t0 = time.time()
    res_astar = astar(graph, deliveries)
    time_astar = time.time() - t0

    t0 = time.time()
    res_ga = genetic_algorithm(graph, deliveries)
    time_ga = time.time() - t0

    t0 = time.time()
    res_aco = aco(graph, deliveries)
    time_aco = time.time() - t0


    print("--- RESULTS ---")

    print("A*:", res_astar, "| time:", round(time_astar, 4))
    print("GA:", res_ga, "| time:", round(time_ga, 4))
    print("ACO:", res_aco, "| time:", round(time_aco, 4))

    algorithms = ["A*", "GA", "ACO"]

    times = [round(time_astar, 4), round(time_ga, 4), round(time_aco, 4)]

    # tempo execução
    plt.figure()
    plt.bar(algorithms, times)
    plt.title("Execution Time Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.savefig("results/time_comparison.png")

    plt.show()

if __name__ == "__main__":
    run_all()

