from algorithms.utils import get_neighbors
import heapq


class AstarManhattan:
    def init(self, initial_state, goal_state):
        self.goal_state = goal_state
        self.frontier = []  # Use a list as a priority queue
        self.explored = set()
        self.frontier_U_explored = set()
        heapq.heappush(self.frontier, (0, initial_state))
        self.parent = {initial_state: (initial_state, 0, 0)}

    def run_algorithm(self) -> bool:
        while self.frontier:
            # Get the node with the lowest key (number)
            cost, node = heapq.heappop(self.frontier)

            if node in self.explored:
                continue

            if self.parent[node][0] == node:  # Root Node
                self.parent[node][2] = self.manhattan(node, 0)

            self.explored.add(node)
            self.frontier_U_explored.add(node)

            if node == self.goal_state:
                return True

            next_states = get_neighbors(node)
            for i in range(len(next_states)):
                heuristic = self.manhattan(next_states[i], self.parent[next_states[i]][2])
                priority = cost + heuristic

                # Update the parent if the new priority is better
                if next_states[i] not in self.frontier_U_explored or priority < self.parent[next_states[i]][1]:
                    self.parent[next_states[i]] = (node, priority, heuristic)
                    heapq.heappush(self.frontier, (priority, next_states[i]))
                    self.frontier_U_explored.add(next_states[i])

        return False

    def manhattan(self, curr_state, prev_state, prev_heuristic):
        zero_curr = int(curr_state[10])
        zero_prev = int(prev_state[10])
        num_prev = zero_curr
        num_curr = zero_prev

        prev_heuristic = prev_heuristic + zero_curr // 3 + zero_curr % 3 + num_curr // 3 + num_curr % 3
        prev_heuristic = prev_heuristic - zero_prev // 3 - zero_prev % 3 - num_prev // 3 - num_prev % 3

        return prev_heuristic
