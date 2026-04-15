import heapq

class State:
    def __init__(self, current, time_now, remaining, bonus):
        self.current = current
        self.time_now = time_now
        self.remaining = remaining
        self.bonus = bonus

    def __lt__(self, other):
        return self.bonus > other.bonus


def heuristic(remaining):
    return sum(d.bonus for d in remaining)


def astar(graph, deliveries):
    start = State('A', 0, deliveries, 0)
    pq = []
    heapq.heappush(pq, (-heuristic(deliveries), start))

    best = 0

    while pq:
        _, state = heapq.heappop(pq)
        best = max(best, state.bonus)

        for d in state.remaining:
            travel = graph.cost(state.current, d.destination)
            arrival = state.time_now + travel

            new_bonus = state.bonus
            new_time = arrival

            if arrival <= d.start_time:
                new_bonus += d.bonus
                new_time = d.start_time

            new_remaining = [x for x in state.remaining if x != d]

            new_state = State(d.destination, new_time, new_remaining, new_bonus)
            score = new_bonus + heuristic(new_remaining)

            heapq.heappush(pq, (-score, new_state))

    return best