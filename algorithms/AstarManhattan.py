from algorithms.utils import get_neighbors, State
import heapq as hq

class AstarManhattan:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.frontier = []
        self.explored = set()
        self.max_depth = 0

    def run_algorithm(self):
        state = State(self.initial_state)
        state.heuristic = self.heuristic(state)
        hq.heappush(self.frontier, state)

        while self.frontier:
            state = hq.heappop(self.frontier)
            self.max_depth = max(self.max_depth, state.depth)

            if state.board in self.explored:
                continue

            self.explored.add(state.board)

            if state.board == self.goal_state:
                return state

            for neighbor in get_neighbors(state):
                if neighbor.board not in self.explored:
                    neighbor.heuristic = self.heuristic(neighbor)
                    hq.heappush(self.frontier, neighbor)

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
