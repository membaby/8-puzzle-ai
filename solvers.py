import time

from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.AstarManhattan import AstarManhattan
from algorithms.AstarEuclidean import AstarEuclidean

class Solver:
    
    def solve(self, algorithm, initial_state, goal_state):
        start_time = time.time()
        if algorithm == '1':
            solver = DFS(initial_state, goal_state)
        elif algorithm == '2':
            solver = BFS(initial_state, goal_state)
        elif algorithm == '3':
            solver = AstarManhattan(initial_state, goal_state)
        elif algorithm == '4':
            solver = AstarEuclidean(initial_state, goal_state)
        solution,parent_map= solver.run_algorithm()
       
        # solution, steps, cost_of_path, nodes_expanded, search_depth = solver.run_algorithm()
        end_time = time.time()
        running_time = round(end_time - start_time, 5)

        #the path to the goal (list of all states)
        list_of_states=[goal_state]
        back_tracked_node=goal_state
        while back_tracked_node!=initial_state and back_tracked_node in parent_map:
            list_of_states.append(parent_map[back_tracked_node])
            back_tracked_node=parent_map[back_tracked_node]
        list_of_states.reverse()
        # return solution, steps, cost_of_path, nodes_expanded, search_depth, running_time
        return solution, running_time,list_of_states