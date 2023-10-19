from rich import print
from rich.table import Table
from solvers import Solver


def print_puzzle(state, prev_state, title):
    table = Table(title=title)
    table.add_column("Parent", justify="center", style="cyan", no_wrap=True)
    table.add_column("Child", justify="center", style="magenta", no_wrap=True)
    for i in range(3):
        table.add_row(' '.join([str(x) for x in state[i]]), ' '.join([str(x) for x in prev_state[i]]))
    print(table)


def print_states(list_of_state):
    for i in range(0, len(list_of_state)):
        state = list_of_state[i]
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print("_____")
        print()


if __name__ == '__main__':
    # Stage 1: Algorithm Selection
    print('.:[ 8-Puzzle Solver ]:.')
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

    # Stage 2: Initial State
    initial_state = ''
    print('[ ] Enter 8-Puzzle Initial State:')
    for i in range(3):
        row = input().replace(' ', '')

        # Invalid Input - Error Handler
        if len(row) != 3:
            print("I can't solve puzzles larger than 3x3.")
            exit()
        elif not all([x.isnumeric() for x in row]):
            print("I can't solve puzzles containing non-numeric values.")
            exit()

        initial_state += row
    initial_state += str(initial_state.index('0'))
    # initial_state example: 1234567808

    # Stage 3: Solvers
    goal_state = '0123456780'
    solver = Solver()
    solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)
    # solution, running_time, list_of_states = solver.solve(user_choice_algorithm, initial_state, goal_state)
    # print('Solution:', solution)
    # print('Time:', running_time)
    # print('path to the goal:')
    # print_states(list_of_states)

    # Stage 4: Results
    print()
    print_states(steps)
    print()
    print('.:[ SOLUTION STATS ]:.')
    print('[ ] [bold]Cost of Path[/bold]:', cost_of_path)
    print('[ ] [bold]Nodes Expanded[/bold]:', nodes_expanded)
    print('[ ] [bold]Search Depth[/bold]:', search_depth)
    print('[ ] [bold]Running Time[/bold]:', running_time)
