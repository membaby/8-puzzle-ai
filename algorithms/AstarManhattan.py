from algorithms.utils import get_neighbors
import heapq as hq
import math
import time

class AstarManhattan:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = [(self.heuristic(initial_state), 0, initial_state, initial_state)]
        self.explored = set()
        self.parent = {}

    def run_algorithm(self):

        while self.frontier:
            _, c, par, current_state = hq.heappop(self.frontier)

            if current_state in self.explored:
                continue

            self.explored.add(current_state)
            self.parent[current_state] = par

            if current_state == self.goal_state:
                return self.parent

            for neighbor in get_neighbors(current_state):
                if neighbor not in self.explored:
                    hq.heappush(self.frontier, (self.heuristic(neighbor)+c+1, c+1, current_state, neighbor))

    def heuristic(self, state):
        h = 0
        for i in range(9):
            goal_x = int(self.goal_state[i]) // 3
            goal_y = int(self.goal_state[i]) % 3
            current_x = int(state[i]) // 3
            current_y = int(state[i]) % 3
            h += abs(goal_x - current_x) + abs(goal_y - current_y)
        return h
