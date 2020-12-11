with open("input.txt", "r") as file:
    lines = file.read().split("\n")

class SEAT_CODE:
    Empty = "L"
    Occupied = "#"
    Floor = "."

def get_grid():
    return [list(line.replace(SEAT_CODE.Empty, SEAT_CODE.Occupied)) for line in lines]

# PART 1

def check(i, j, grid, state):
    occ = check_n(i, j, grid) + check_s(i, j, grid) + check_w(i, j, grid) + check_e(i, j, grid)

    if state == SEAT_CODE.Occupied:
        if occ >= 4:
            return SEAT_CODE.Empty, False
        return SEAT_CODE.Occupied, True
    if occ >= 1:
        return SEAT_CODE.Empty, True
    return SEAT_CODE.Occupied, False

def check_n(i, j, grid):
    previous_row = i - 1
    neighbors = 0
    if previous_row >= 0:
        line = grid[previous_row]
        pattern = line[j]
        neighbors += 1 if pattern == SEAT_CODE.Occupied else 0

        if j-1 >= 0:
            pattern = line[j-1]
            neighbors += 1 if pattern == SEAT_CODE.Occupied else 0

        if j+1 <= len(line)-1:
            pattern = line[j+1]
            neighbors += 1 if pattern == SEAT_CODE.Occupied else 0
    return neighbors

def check_s(i, j, grid):
    next_row = i + 1
    neighbors = 0
    if next_row < len(grid):
        line = grid[next_row]
        pattern = line[j]
        neighbors += 1 if pattern == SEAT_CODE.Occupied else 0

        if j-1 >= 0:
            pattern = line[j-1]
            neighbors += 1 if pattern == SEAT_CODE.Occupied else 0

        if j+1 <= len(line)-1:
            pattern = line[j+1]
            neighbors += 1 if pattern == SEAT_CODE.Occupied else 0
    return neighbors

def check_w(i, j, grid):
    previous_col = j - 1
    if previous_col >= 0:
        pattern = grid[i][previous_col]
        return 1 if pattern == SEAT_CODE.Occupied else 0
    return 0

def check_e(i, j, grid):
    next_col = j+1
    if next_col < len(grid[0]):
        pattern = grid[i][next_col]
        return 1 if pattern == SEAT_CODE.Occupied else 0
    return 0


old_grid = get_grid()
no_changes = False
while not no_changes:
    new_grid, no_changes = [], True
    nr_occupied = 0
    for row, line in enumerate(old_grid):
        new_grid.append([])
        for col, seat in enumerate(line):
            if seat == SEAT_CODE.Floor:
                new_grid[-1].append(SEAT_CODE.Floor)
                continue
            new_state, is_stationary = check(row, col, old_grid, seat)
            if new_state == SEAT_CODE.Occupied:
                nr_occupied += 1
            no_changes &= is_stationary
            new_grid[-1].append(new_state)
    old_grid = new_grid

print("PART 1 - Number of occupied seats : " + str(nr_occupied))

# PART 2

def check(i, j, grid, state):
    neighbors = [None]*8
    offset = 1
    while neighbors.count(None) > 0:
        check_n(i, j, offset, grid, neighbors)
        check_s(i, j, offset, grid, neighbors)
        check_w(i, j, offset, grid, neighbors)
        check_e(i, j, offset, grid, neighbors)

        occ = neighbors.count(SEAT_CODE.Occupied)
        if state == SEAT_CODE.Occupied:
            if occ >= 5:
                return SEAT_CODE.Empty, False
            empt = neighbors.count(SEAT_CODE.Empty)
            if empt >= 4:
                return SEAT_CODE.Occupied, True
        else:
            if occ >= 1:
                return SEAT_CODE.Empty, True
        offset += 1
    return SEAT_CODE.Occupied, False

def check_n(i, j, offset, grid, neighbors):
    previous_row = i - offset
    if previous_row < 0:
        neighbors[0] = SEAT_CODE.Empty if not neighbors[0] else neighbors[0]
        neighbors[1] = SEAT_CODE.Empty if not neighbors[1] else neighbors[1]
        neighbors[2] = SEAT_CODE.Empty if not neighbors[2] else neighbors[2]
        return
    line = grid[previous_row]
    if neighbors[1] is None:
        pattern = line[j]
        neighbors[1] = pattern if pattern != SEAT_CODE.Floor else None

    if neighbors[0] is None:
        if j-offset == -1:
            neighbors[0] = SEAT_CODE.Empty
        elif j-offset >= 0:
            pattern = line[j-offset]
            neighbors[0] = pattern if pattern != SEAT_CODE.Floor else None

    if neighbors[2] is None:
        if j+offset == len(line):
           neighbors[2] = SEAT_CODE.Empty
        elif j+offset <= len(line)-1:
            pattern = line[j+offset]
            neighbors[2] = pattern if pattern != SEAT_CODE.Floor else None

def check_s(i, j, offset, grid, neighbors):
    next_row = i + offset
    if next_row >= len(grid):
        neighbors[4] = SEAT_CODE.Empty if not neighbors[4] else neighbors[4]
        neighbors[5] = SEAT_CODE.Empty if not neighbors[5] else neighbors[5]
        neighbors[6] = SEAT_CODE.Empty if not neighbors[6] else neighbors[6]
        return
    line = grid[next_row]
    if neighbors[5] is None:
        pattern = line[j]
        neighbors[5] = pattern if pattern != SEAT_CODE.Floor else None
    if neighbors[6] is None:
        if j-offset == -1:
            neighbors[6] = SEAT_CODE.Empty
        elif j-offset >= 0:
            pattern = line[j-offset]
            neighbors[6] = pattern if pattern != SEAT_CODE.Floor else None
    if neighbors[4] is None:
        if j+offset == len(line):
           neighbors[4] = SEAT_CODE.Empty
        elif j+offset <= len(line)-1:
            pattern = line[j+offset]
            neighbors[4] = pattern if pattern != SEAT_CODE.Floor else None

def check_w(i,j,offset,grid,neighbors):
    previous_col = j - offset
    if previous_col < 0 and neighbors[7] is None:
        neighbors[7] = SEAT_CODE.Empty
        return
    if neighbors[7] is None:
        pattern = grid[i][previous_col]
        neighbors[7] = pattern if pattern != SEAT_CODE.Floor else None

def check_e(i,j,offset,grid, neighbors):
    next_col = j+offset
    if next_col >= len(grid[0]) and neighbors[3] is None:
        neighbors[3] = SEAT_CODE.Empty
        return
    if neighbors[3] is None:
        pattern = grid[i][next_col]
        neighbors[3] = pattern if pattern != SEAT_CODE.Floor else None

old_grid = get_grid()
no_changes = False
while not no_changes:
    new_grid, no_changes = [], True
    nr_occupied = 0
    for row, line in enumerate(old_grid):
        new_grid.append([])
        for col, seat in enumerate(line):
            if seat == SEAT_CODE.Floor:
                new_grid[-1].append(SEAT_CODE.Floor)
                continue
            new_state, has_changed = check(row, col, old_grid, seat)
            if new_state == SEAT_CODE.Occupied:
                nr_occupied += 1
            no_changes &= has_changed
            new_grid[-1].append(new_state)
    old_grid = new_grid

print("PART 2 - Number of occupied seats : " + str(nr_occupied))