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
        solutions.append([initial_state, solution, running_time])
        if solution:
            print(f'Solution found for {initial_state}.')
        else:
            print(f'No solution found for {initial_state}.')
    except Exception as err:
        print(f'Error occured while solving {initial_state}.')
        print(err)
        quit()

if __name__ == '__main__':
    print('.:[ 8-Puzzle Batch Solver ]:.')
    print('[ ] Please select an algorithm:')
    print('     [-] Uninformed Search Methods:')
    print('         [1] Depth-First Search')
    print('         [2] Breadth-First Search')
    print('     [-] Informed Search Methods:')
    print('         [3] A* Search - Manhattan Distance')
    print('         [4] A* Search - Euclidean Distance')

    while True:
        user_choice_algorithm = input('Your Choice: ')
        if user_choice_algorithm in ['1', '2', '3', '4']: break
        print('[!] Invalid choice.')

    sample_size = int(input('Enter sample size: '))
    
    solutions = []
    solver = Solver()
    test_cases = [x.strip() for x in open('tests/tests.txt', 'r')]
    sample = random.sample(test_cases, sample_size)
    goal_state = '0123456780'

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    for initial_state in sample:
        executor.submit(run_thread, solver, user_choice_algorithm, initial_state, goal_state)
    executor.shutdown(wait=True)

    with open('tests/results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Initial State', 'Solution', 'Running Time'])
        for solution in solutions:
            writer.writerow(solution)