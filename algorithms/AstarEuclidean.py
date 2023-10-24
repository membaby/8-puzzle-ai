from algorithms.utils import get_neighbors, State
import heapq as hq
import math


class AstarEuclidean:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.initial_state = initial_state
        self.frontier = []
        self.explored = set()
        self.max_depth = 0
        self.frontier_U_explored = set()
        self.depth_map = {initial_state: 0}

    def run_algorithm(self):
        state = State(self.initial_state)
        self.initial_heuristic(state)
        hq.heappush(self.frontier, state)
        self.frontier_U_explored.add(state.board)

        while self.frontier:
            state = hq.heappop(self.frontier)
            self.max_depth = max(self.max_depth, state.depth)

            if state.board in self.explored:
                continue

            self.explored.add(state.board)

            if state.board == self.goal_state:
                return state

            for neighbor in get_neighbors(state):
                if neighbor.board not in self.frontier_U_explored:
                    self.heuristic(state, neighbor)
                    hq.heappush(self.frontier, neighbor)
                    self.depth_map[neighbor.board] = neighbor.depth
                    self.frontier_U_explored.add(neighbor.board)
                elif neighbor.board not in self.explored and neighbor.depth < self.depth_map[neighbor.board]:
                    self.heuristic(state, neighbor)
                    hq.heappush(self.frontier, neighbor)
                    self.depth_map[neighbor.board] = neighbor.depth

        return False

    def initial_heuristic(self, state):
        h = 0
        for i in range(9):
            if state.board[i] != '0':
                h += self.euclidean(i, state.board[i])
        state.heuristic = h

    def heuristic(self, prev_state, curr_state):
        h = prev_state.heuristic
        key1 = int(prev_state.board[-1])
        key2 = int(curr_state.board[-1])
        h -= self.euclidean(key2, prev_state.board[key2])
        h += self.euclidean(key1, curr_state.board[key1])
        curr_state.heuristic = h

    def euclidean(self, key, num):
        current_x = key // 3
        current_y = key % 3
        goal_x = int(self.goal_state[int(num)]) // 3
        goal_y = int(self.goal_state[int(num)]) % 3
        return math.sqrt((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2)
