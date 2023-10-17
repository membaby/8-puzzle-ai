import time

from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.Astar import Astar

class Solver:

    def solve(self, algorithm, initial_state):
        start_time = time.time()
        if algorithm == '1':
            solver = DFS(initial_state)
        elif algorithm == '2':
            solver = BFS(initial_state)
        elif algorithm == '3':
            solver = Astar(initial_state)
        solution, steps, cost_of_path, nodes_expanded, search_depth = solver.run_algorithm()
        end_time = time.time()

        running_time = round(end_time - start_time, 5)
        return solution, steps, cost_of_path, nodes_expanded, search_depth, running_time