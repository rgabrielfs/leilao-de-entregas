import random
import math
import heapq
import time

class Delivery:
    def __init__(self, destination, start_time, bonus):
        self.destination = destination
        self.start_time = start_time
        self.bonus = bonus

    def __repr__(self):
        return f"Delivery({self.destination}, t={self.start_time}, b={self.bonus})"
