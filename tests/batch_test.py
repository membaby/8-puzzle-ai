import sys
import os

# Add the parent directory to the sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from solvers import Solver
from rich import print
import random
import csv
import concurrent.futures

def run_thread(solver, user_choice_algorithm, initial_state, goal_state):
    try:
        solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
        solutions[user_choice_algorithm][initial_state] = [solution, len(steps), nodes_expanded, search_depth, running_time]
        if solution:
            print(f'Solution found for {initial_state}.')
        else:
            print(f'No solution found for {initial_state}.')
    except Exception as err:
        print(f'Error occured while solving {initial_state}.')
        print(err)
        quit()

if __name__ == '__main__':
    sample_size = int(input('Enter sample size: '))
    solutions = {'1': {},'2': {},'3': {},'4': {}}
    solver = Solver()
    test_cases = [x.strip() for x in open('tests.txt', 'r')]
    sample = random.sample(test_cases, sample_size)
    goal_state = '0123456780'

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    for initial_state in sample:
        executor.submit(run_thread, solver, '1', initial_state, goal_state)
        executor.submit(run_thread, solver, '2', initial_state, goal_state)
        executor.submit(run_thread, solver, '3', initial_state, goal_state)
        executor.submit(run_thread, solver, '4', initial_state, goal_state)
    executor.shutdown(wait=True)

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Initial State'] + ['Solution', 'Steps', 'Nodes Expanded', 'Search Depth', 'Running Time'] * 4)
        for initial_state in solutions['1']:
            row = []
            row.append(initial_state)
            for algorithm in solutions:
                row.extend(solutions[algorithm][initial_state])
            writer.writerow(row)