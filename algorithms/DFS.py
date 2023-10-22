from algorithms.utils import get_neighbors
from collections import deque

class DFS:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = deque([initial_state])
        self.explored = set()
        self.frontier_U_explored = set()
        self.parent_map={initial_state:initial_state} #dictionary

    def run_algorithm(self):
        while self.frontier:
            state = self.frontier.pop()
            self.explored.add(state)
            self.frontier_U_explored.add(state)

            if state == self.goal_state:
                return True
        
            for neighbor in get_neighbors(state)[::-1]:
                if neighbor not in self.frontier_U_explored:
                    self.frontier.append(neighbor)   
                    self.frontier_U_explored.add(neighbor)
                    self.parent_map[neighbor]=state
        return False