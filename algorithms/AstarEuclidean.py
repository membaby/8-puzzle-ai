from algorithms.utils import get_neighbors
import heapq as hq
import math


class AstarEuclidean:
    def __init__(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = [(self.heuristic(initial_state), 0, initial_state, initial_state)]
        self.explored = set()
        self.parent_map = {}

    def run_algorithm(self):

        while self.frontier:
            _, c, par, current_state = hq.heappop(self.frontier)

            if current_state in self.explored:
                continue

            self.explored.add(current_state)
            self.parent_map[current_state] = par

            if current_state == self.goal_state:
                return

            for neighbor in get_neighbors(current_state):
                if neighbor not in self.explored:
                    hq.heappush(self.frontier, (self.heuristic(neighbor) + c + 1, c + 1, current_state, neighbor))

    def heuristic(self, state):
        h = 0
        for i in range(9):
            goal_x = int(self.goal_state[i]) // 3
            goal_y = int(self.goal_state[i]) % 3
            current_x = int(state[i]) // 3
            current_y = int(state[i]) % 3
            h += math.sqrt((goal_x - current_x) ** 2 + (goal_y - current_y) ** 2)
        return h


# initial_state = "1423056784"
# goal_state = "1234567808"
# solver = AstarEuclidean(initial_state, goal_state)
# par = solver.run_algorithm()
# print(par)
# print(len(par))
# path = []
# cur = goal_state
# while par[cur] != cur:
#     path.append(cur)
#     cur = par[cur]
# path.append(initial_state)
# path.reverse()
# print(path)
# print(len(path))
