import itertools


def join(row):
    return "".join(row)


def bomberPlane(n, grid):
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
        # for row in zeros_grid:
        #     zeros_grid_of_strings.append("".join(sublist))
        return ["".join(zeros_grid)]
