import itertools


def join(row):
    return "".join(row)


def get_zeros_grid(r, c):
    # create a list of sublists of zeros, with the same number of rows and columns as the initial grid
    return [["O" for i in range(c)] for x in itertools.repeat(None, r)]


# O represents a bomb. . represents a cell without a bomb
def bomberPlane(n, grid):
    if n < 2:
        return grid  # nothing changes in grid until after 2 seconds

    r = len(grid)  # number of rows in grid. 6 in our example
    c = len(grid[0])  # number of characters in each row. 7 in our example

    if n % 2 == 0:  # every 2 seconds, bombs are added to every cell i.e. all zeros
        zeros_grid = get_zeros_grid(r, c)
        joinedList = list(
            map(join, zeros_grid)
        )  # map does not alter the original array, so zeros_grid is still a grid like [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]
        return joinedList

    grid_after_3_seconds = get_zeros_grid(r, c)
    for i in range(r):  # range is exclusive of r
        for j in range(c):  # range is exclusive of c
            if grid[i][j] == "O":
                grid_after_3_seconds[i][j] = "."
                if (
                    i < r - 1
                ):  # check that i is not at the last row which would made i+1 index outside the grid(causing index out of range error)
                    grid_after_3_seconds[i + 1][j] = "."
                if i > 0:
                    grid_after_3_seconds[i - 1][j] = "."
                if (
                    j < c - 1
                ):  # check that j is not at the last column which would made j+1 index outside the grid (causing index out of range error)
                    grid_after_3_seconds[i][j + 1] = "."
                if j > 0:
                    grid_after_3_seconds[i][j - 1] = "."
            j += 1
        i += 1

    if n % 4 == 3:  # when n = 3, 7, 11, 15 etc
        joinedList = list(map(join, grid_after_3_seconds))
        return joinedList

    # if we have bypassed all the above if statements, then n % 4 = 1 i.e. n = 5, 9, 13, 17 etc.
    # to calculate the grid after 5 seconds, we look at the grid after 3 seconds: all the remaining O cells represent the bombs planted after 2 seconds so are due to detonate after 5 seconds
    grid_after_5_seconds = get_zeros_grid(r, c)
    print(grid_after_5_seconds)
    for i in range(r):  # range is exclusive of r
        # print(f"i count (row): {i}")
        for j in range(c):  # range is exclusive of c
            # print(f"i(row): {i}, j (column): {j}")
            if grid_after_3_seconds[i][j] == "O":
                grid_after_5_seconds[i][j] = "."
                if (
                    i < r - 1
                ):  # check that i is not at the last row which would made i+1 index outside the grid(causing index out of range error)
                    grid_after_5_seconds[i + 1][j] = "."
                if i > 0:
                    grid_after_5_seconds[i - 1][j] = "."
                if (
                    j < c - 1
                ):  # check that j is not at the last column which would made j+1 index outside the grid (causing index out of range error)
                    grid_after_5_seconds[i][j + 1] = "."
                if j > 0:
                    grid_after_5_seconds[i][j - 1] = "."
            j += 1
        i += 1

    print(grid_after_5_seconds)
    grid_after_5_seconds_joined = list(map(join, grid_after_5_seconds))
    return grid_after_5_seconds_joined


print(f'2 seconds: {bomberPlane(2, ["O..O", ".O..", "...."])}')

# note the recurring pattern. Grid after 5,7,11, 13 always the same
print(
    f'3 seconds: {bomberPlane(3, ["O..O", ".O..", "...."])}'
)  # ['....', '....', 'O.OO'] # any zeros here, were planted after 2 seconds, so will detonate after 5 seconds
print(f'5 seconds: {bomberPlane(5, ["O..O", ".O..", "...."])}')  # ['OOOO', '.O..', '....']
print(f'7 seconds: {bomberPlane(7, ["O..O", ".O..", "...."])}')  # ['....', '....', 'O.OO']
print(f'9 seconds: {bomberPlane(9, ["O..O", ".O..", "...."])}')  # ['OOOO', '.O..', '....']
print(f'11 seconds: {bomberPlane(11, ["O..O", ".O..", "...."])}')  # ['....', '....', 'O.OO']
print(f'13 seconds: {bomberPlane(13, ["O..O", ".O..", "...."])}')  # ['OOOO', '.O..', '....']
