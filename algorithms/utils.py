def get_neighbors(board_str) -> list:
    key = int(board_str[-1])
    rows, cols = 3, 3
    row = key // cols
    col = key % cols
    neighbors = []
    if row > 0:
        neighbors.append(move_up(board_str))
    if row < rows - 1:
        neighbors.append(move_down(board_str))
    if col > 0:
        neighbors.append(move_left(board_str))
    if col < cols - 1:
        neighbors.append(move_right(board_str))
    return neighbors

def move_up(board_str):
    key = int(board_str[-1])
    if key < 3: return None
    board_list = list(board_str)
    board_list[key], board_list[key - 3] = board_list[key - 3], board_list[key]
    board_list[-1] = str(key - 3)
    return ''.join(board_list)

def move_down(board_str):
    key = int(board_str[-1])
    if key > 5: return None
    board_list = list(board_str)
    board_list[key], board_list[key + 3] = board_list[key + 3], board_list[key]
    board_list[-1] = str(key + 3)
    return ''.join(board_list)

def move_left(board_str):
    key = int(board_str[-1])
    if key % 3 == 0: return None
    board_list = list(board_str)
    board_list[key], board_list[key - 1] = board_list[key - 1], board_list[key]
    board_list[-1] = str(key - 1)
    return ''.join(board_list)

def move_right(board_str):
    key = int(board_str[-1])
    if key % 3 == 2: return None
    board_list = list(board_str)
    board_list[key], board_list[key + 1] = board_list[key + 1], board_list[key]
    board_list[-1] = str(key + 1)
    return ''.join(board_list)

def is_solvable(state):
    inversion_count = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] != '0' and state[j] != '0' and state[i] > state[j]:
                inversion_count += 1
    return inversion_count % 2 == 0 #true when it is even

# 1 2 3
# 0 4 5
# 6 7 8

# neighbors = get_neighbors('1230456783')
# for neighbor in neighbors:
#     print(neighbor[:3])
#     print(neighbor[3:6])
#     print(neighbor[6:9])
#     print(neighbor[-1])
#     print()