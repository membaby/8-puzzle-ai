from algorithms.utils import get_neighbors, State
import heapq as hq
import math
import time

class AstarManhattan:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.frontier = []
        self.explored = set()
        self.max_depth = 0
        # self.parent_map = {}

    def run_algorithm(self):
        state = State(self.initial_state)
        hq.heappush(self.frontier, (self.heuristic(state), 0, state, state))
        while self.frontier:
            _, c, par, state = hq.heappop(self.frontier)

            if state.board in self.explored:
                continue

            self.explored.add(state.board)
            # self.parent_map[current_state] = par

            if state.board == self.goal_state:
                return state

            for neighbor in get_neighbors(state):
                if neighbor.board not in self.explored:
                    hq.heappush(self.frontier, (self.heuristic(neighbor) + c + 1, c + 1, state, neighbor))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return False
        
    def heuristic(self, state):
        h = 0
        for i in range(9):
            goal_x = int(self.goal_state[i]) // 3
            goal_y = int(self.goal_state[i]) % 3
            current_x = int(state.board[i]) // 3
            current_y = int(state.board[i]) % 3
            h += abs(goal_x - current_x) + abs(goal_y - current_y)
        return h
