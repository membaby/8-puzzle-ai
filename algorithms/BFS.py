from algorithms.utils import get_neighbors, State
from collections import deque

class BFS:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.frontier = deque()
        self.explored = set()
        self.frontier_U_explored = set()
        self.max_depth = 0
        # self.parent_map={initial_state:initial_state} #dictionary

    def run_algorithm(self):
        self.frontier.append(State(self.initial_state))
        while len(self.frontier)!=0:
            state = self.frontier.popleft()
            self.max_depth = max(self.max_depth, state.depth)
            self.explored.add(state.board)
            self.frontier_U_explored.add(state.board)

            if state.board == self.goal_state:
                return state
            
            for neighbor in get_neighbors(state):
                 if neighbor.board not in self.frontier_U_explored:
                     self.frontier.append(neighbor)
                     self.frontier_U_explored.add(neighbor.board)
        return False