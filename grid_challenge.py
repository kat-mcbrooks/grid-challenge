import itertools


def join(row):
    return "".join(row)


def bomberPlane(n, grid):
    if n < 2:
        return grid  # nothing changes in grid until after 2 seconds

    r = len(grid)  # number of rows in grid. 6 in our example
    c = len(grid[0])  # number of characters rather than length of list. 7 in our example
    # print(r, c)
    #
    if n % 2 == 0:  # every 2 seconds, bombs are added to every cell i.e. all zeros
        # create a list of sublists of zeros, with the same number of rows and columns as the initial grid
        zeros_grid = [["O" for i in range(c)] for x in itertools.repeat(None, r)]
        # print(zeros_grid)

        modifiedList = list(map(join, zeros_grid))
        print(modifiedList)
        return modifiedList

    for seconds in range(3, n + 1, 2):
        # create a list of sublists of zeros, with the same number of rows and columns as the initial grid
        zeros_grid = [["O" for i in range(c)] for x in itertools.repeat(None, r)]
        new_grid = zeros_grid
        print(f"new_grid = {new_grid}")
        print(f"grid_list = {grid}")
        for i in range(r):  # range is exclusive of r
            # print(f"i count (row): {i}")
            for j in range(c):  # range is exclusive of c
                # print(f"i(row): {i}, j (column): {j}")
                if grid[i][j] == "O":
                    new_grid[i][j] = "."
                    if (
                        i < r - 1
                    ):  # check that i is not at the last row which would made i+1 index outside the grid(causing index out of range error)
                        new_grid[i + 1][j] = "."
                    if i > 0:
                        new_grid[i - 1][j] = "."
                    if (
                        j < c - 1
                    ):  # check that j is not at the last column which would made j+1 index outside the grid (causing index out of range error)
                        new_grid[i][j + 1] = "."
                    if j > 0:
                        new_grid[i][j - 1] = "."
                    # print(f"after a loop over one row: {new_grid}")
                j += 1
            i += 1
        # print(grid_list)
        # print(f"new_grid line 43= {new_grid}")
        grid = new_grid
        # print(f"grid_list line 44= {grid_list}")
        print(f"after {seconds} seconds:")
        # seconds += 2
    print(grid)
    grid_of_strings = []
    for lst in grid:
        grid_of_strings.append("".join(lst))
    print(grid_of_strings)
    return grid_of_strings
