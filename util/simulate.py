def simulate_route(graph, deliveries, route):
    time_now = 0
    current = 'A'
    total_bonus = 0

    for d in route:
        travel = graph.cost(current, d.destination)
        arrival = time_now + travel

        if arrival <= d.start_time:
            time_now = d.start_time
            total_bonus += d.bonus
        else:
            time_now = arrival

        current = d.destination

    return total_bonus