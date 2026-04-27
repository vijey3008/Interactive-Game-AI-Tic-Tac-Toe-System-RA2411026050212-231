DEFAULT_PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_safe(grid, row, col, num):
    if any(grid[row][c] == num for c in range(9)):
        return False
    if any(grid[r][col] == num for r in range(9)):
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == num:
                return False
    return True

def find_empty_cell_with_mrv(grid):
    best = None
    best_options = None
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                options = [n for n in range(1, 10) if is_safe(grid, r, c, n)]
                if best is None or len(options) < len(best_options):
                    best = (r, c)
                    best_options = options
                if best_options == []:
                    return best, []
    return best, best_options

def solve_sudoku(grid):
    cell, options = find_empty_cell_with_mrv(grid)
    if cell is None:
        return True
    row, col = cell
    for num in options:
        grid[row][col] = num
        if solve_sudoku(grid):
            return True
        grid[row][col] = 0
    return False

def is_valid_solution(grid):
    if not grid or len(grid) != 9 or any(len(row) != 9 for row in grid):
        return False
    target = set(range(1, 10))
    for row in grid:
        if set(row) != target:
            return False
    for c in range(9):
        if set(grid[r][c] for r in range(9)) != target:
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            values = []
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    values.append(grid[r][c])
            if set(values) != target:
                return False
    return True
