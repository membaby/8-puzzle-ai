from algorithms.utils import get_neighbors
from collections import deque

class AstarManhattan:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = deque([initial_state])
        self.explored = set()
        self.frontier_U_explored = set()

    def run_algorithm(self) ->bool:
        ...
        # WRITE ALGORITHM HERE