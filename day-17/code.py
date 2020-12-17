with open("input.txt", "r") as file:
    lines = file.read().split("\n")

ALIVE = "#"
DEAD = "."
NR_BOOT_CYCLES = 6

# INIT

padding = DEAD*(len(lines[0]) + 2)
old_grid = [padding]
old_grid += [DEAD+line+DEAD for line in lines]
old_grid += [padding]

old_grids = [old_grid, [padding for i in range(len(padding))]]

def check_2D(i, j, grid):
    return check_2D_n(i, j, grid) + check_2D_s(i, j, grid) + check_2D_w(i, j, grid) + check_2D_e(i, j, grid)

def check_2D_n(i, j, grid):
    previous_row = i - 1
    neighbors = 0
    if previous_row >= 0:
        line = grid[previous_row]
        pattern = line[j]
        neighbors += 1 if pattern == ALIVE else 0

        if j-1 >= 0:
            pattern = line[j-1]
            neighbors += 1 if pattern == ALIVE else 0

        if j+1 <= len(line)-1:
            pattern = line[j+1]
            neighbors += 1 if pattern == ALIVE else 0
    return neighbors

def check_2D_s(i, j, grid):
    next_row = i + 1
    neighbors = 0
    if next_row < len(grid):
        line = grid[next_row]
        pattern = line[j]
        neighbors += 1 if pattern == ALIVE else 0

        if j-1 >= 0:
            pattern = line[j-1]
            neighbors += 1 if pattern == ALIVE else 0

        if j+1 <= len(line)-1:
            pattern = line[j+1]
            neighbors += 1 if pattern == ALIVE else 0
    return neighbors

def check_2D_w(i, j, grid):
    previous_col = j - 1
    if previous_col >= 0:
        pattern = grid[i][previous_col]
        return 1 if pattern == ALIVE else 0
    return 0

def check_2D_e(i, j, grid):
    next_col = j+1
    if next_col < len(grid[0]):
        pattern = grid[i][next_col]
        return 1 if pattern == ALIVE else 0
    return 0

def check_3D_a(i, j, grid):
    occ = check_2D(i, j, grid)
    return occ + (1 if grid[i][j] == ALIVE else 0)

def check_3D(i, j, k, grids, state):
    nr_alive = check_2D(i, j, grids[k])
    if k+1 < len(grids):
        nr_alive += check_3D_a(i, j, grids[k+1])
    
    if abs(k-1) < len(grids):
        nr_alive += check_3D_a(i, j, grids[abs(k-1)])

    return nr_alive

def get_next_state(nr_alive, state):
    if state == ALIVE:
        if nr_alive == 2 or nr_alive == 3:
            return ALIVE
        return DEAD
    if nr_alive == 3:
        return ALIVE
    return DEAD

def execute_new_cycle(old_grids):
    nr_alive, new_grids = 0, []
    for layer, grid in enumerate(old_grids):
        padding = DEAD*(len(old_grids[0]) + 2)
        new_grid = [padding]
        for row, line in enumerate(old_grids[layer]):
            new_grid.append(DEAD)
            for col, state in enumerate(line):
                neighbors_alive = check_3D(row, col, layer, old_grids, state)
                new_state = get_next_state(neighbors_alive, state)
                if new_state == ALIVE:
                    nr_alive += 1 if layer == 0 else 2
                new_grid[-1] += new_state
            new_grid[-1] += DEAD
        new_grid.append(padding)
        new_grids.append(new_grid)
    new_grids.append([padding for i in range(len(padding))])
    return nr_alive, new_grids

for cycle in range(NR_BOOT_CYCLES): 
    nr_alive, old_grids = execute_new_cycle(old_grids)
print(nr_alive)

# PART 2

