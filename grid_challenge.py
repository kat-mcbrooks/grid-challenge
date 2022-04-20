import itertools


def bomberPlane(n, grid):
    r = len(grid)  # number of rows in grid. 6 in our example
    c = len(grid[0])  # number of characters rather than length of list. 7 in our example
    # print(r, c)
    #
    if n % 2 == 0:  # every 2 seconds, bombs are added to every cell i.e. all zeros
        # create a list of sublists of zeros, with the same number of rows and columns as the initial grid
        zeros_grid = ["O" for i in range(c) for x in itertools.repeat(None, r)]
        print(zeros_grid)
        return ["".join(zeros_grid)]
