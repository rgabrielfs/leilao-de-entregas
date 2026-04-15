class Graph:
    def __init__(self, adjacency):
        self.adjacency = adjacency

    def cost(self, a, b):
        return self.adjacency[a][b]
