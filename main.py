from rich import print
from rich.table import Table
from solvers import Solver


def print_puzzle(state, prev_state, title):
    table = Table(title=title)
    table.add_column("Parent", justify="center", style="cyan", no_wrap=True)
    table.add_column("Child", justify="center", style="magenta", no_wrap=True)
    for i in range(3):
        table.add_row(' '.join([str(x) for x in state[i*3:(i+1)*3]]), ' '.join([str(x) for x in prev_state[i*3:(i+1)*3]]))
    print(table)

def get_movement(from_state, to_state):
    zero_index_from = from_state.index('0')
    zero_index_to = to_state.index('0')
    if zero_index_from == zero_index_to + 1:
        return 'Right'
    elif zero_index_from == zero_index_to - 1:
        return 'Left'
    elif zero_index_from == zero_index_to + 3:
        return 'Down'
    elif zero_index_from == zero_index_to - 3:
        return 'Up'
    else:
        return 'Invalid'


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

    if '0' not in initial_state:
        print("I can't solve puzzles without a blank tile.")
        exit()
    elif initial_state.count('0') > 1:
        print("I can't solve puzzles with more than one blank tile.")
        exit()

    initial_state += str(initial_state.index('0'))

    # Stage 3: Solvers
    goal_state = '0123456780'
    solver = Solver()
    solution, steps, cost_of_path, nodes_expanded, search_depth, running_time = solver.solve(user_choice_algorithm, initial_state, goal_state)

    # Stage 4: Results
    print()
    movements = []
    if solution:
        PRINT_STEPS = True  # Set to False to disable printing steps
        if steps and PRINT_STEPS:
            for i in range(len(steps)):
                if i == len(steps) - 1: break
                movement = get_movement(steps[i+1], steps[i])
                movements.append(movement)
                print_puzzle(steps[i], steps[i+1], f'Step {i + 1}: {movement}')
        elif steps:
            print_puzzle(steps[0], steps[-1], 'Initial & Goal')
    else:
        print('[red][!][/red] No solution found.')
    print()
    print('.:[ SOLUTION STATS ]:.')
    print('• [bold]Path[/bold]:', ' -> '.join(movements))
    print('• [bold]Cost of Path[/bold]:', cost_of_path)
    print('• [bold]Nodes Expanded[/bold]:', nodes_expanded)
    print('• [bold]Search Depth[/bold]:', search_depth)
    print('• [bold]Running Time[/bold]:', running_time)
