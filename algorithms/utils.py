def get_neighbors(state) -> list:
    key = int(state.board[-1])
    rows, cols = 3, 3
    row = key // cols
    col = key % cols
    neighbors = []
    if row > 0:
        neighbors.append(move_up(state))
    if col > 0:
        neighbors.append(move_left(state))
    if row < rows - 1:
        neighbors.append(move_down(state))
    if col < cols - 1:
        neighbors.append(move_right(state))
    return neighbors

def move_up(state):
    key = int(state.board[-1])
    if key < 3:
        return None
    board_list = list(state.board)
    board_list[key], board_list[key - 3] = board_list[key - 3], board_list[key]
    board_list[-1] = str(key - 3)
    return State(''.join(board_list), state, state.depth + 1)

def move_down(state):
    key = int(state.board[-1])
    if key > 5:
        return None
    board_list = list(state.board)
    board_list[key], board_list[key + 3] = board_list[key + 3], board_list[key]
    board_list[-1] = str(key + 3)
    return State(''.join(board_list), state, state.depth + 1)

def move_left(state):
    key = int(state.board[-1])
    if key % 3 == 0:
        return None
    board_list = list(state.board)
    board_list[key], board_list[key - 1] = board_list[key - 1], board_list[key]
    board_list[-1] = str(key - 1)
    return State(''.join(board_list), state, state.depth + 1)

def move_right(state):
    key = int(state.board[-1])
    if key % 3 == 2:
        return None
    board_list = list(state.board)
    board_list[key], board_list[key + 1] = board_list[key + 1], board_list[key]
    board_list[-1] = str(key + 1)
    return State(''.join(board_list), state, state.depth + 1)

def is_solvable(state):
    inversion_count = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if state[i] != '0' and state[j] != '0' and state[i] > state[j]:
                inversion_count += 1
    return inversion_count % 2 == 0  # true when it is even

class State:
    def __init__(self, board, parent=None, depth=0, heuristic=0):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.depth + self.heuristic < other.depth + other.heuristic
