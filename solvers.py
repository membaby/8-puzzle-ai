import time

from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.AstarManhattan import AstarManhattan
from algorithms.AstarEuclidean import AstarEuclidean
from algorithms.utils import is_solvable


class Solver:

    @staticmethod
    def solve(algorithm, initial_state, goal_state):
        if algorithm == '1':
            solver = DFS(initial_state, goal_state)
        elif algorithm == '2':
            solver = BFS(initial_state, goal_state)
        elif algorithm == '3':
            solver = AstarManhattan(initial_state, goal_state)
        else:
            solver = AstarEuclidean(initial_state, goal_state)
        res = False
        start_time = time.time()
        solution = is_solvable(initial_state)
        if solution:
            res = solver.run_algorithm()
        end_time = time.time()
        expanded = solver.explored
        running_time = round(end_time - start_time, 5)

        if res:
            # the path to the goal (list of all states)
            steps = [res.board]
            while res.parent is not None:
                steps.append(res.parent.board)
                res = res.parent
            steps.reverse()
            return solution, steps, len(steps)-1, len(expanded), solver.max_depth, running_time

        return solution, [], 0, len(expanded), solver.max_depth, running_time
