# Grid Challenge aka HackerRank's BomberPlane challenge

### Challenge instructions, slightly modified in my own words:

BomberPlane plants bombs in a rectangular grid. Each cell in the grid can either contain a bomb ('O') or nothing at all('.').

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell i,j , the cell above (i+1,j), below(i-1,j) left (i, j-1) and right (i, j+1) are also cleared (turning cells to '.'). If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

BomberPlane takes these actions, as each second passes:

0. Initially, BomberPlane arbitrarily plants bombs in some of the cells, the initial state. This will be the grid passed in as an argument
1. After one second, BomberPlane does nothing. (aka the grid stays the same.)
2. After one more second, BomberPlane plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
3. After one more second, any bombs planted exactly three seconds ago will detonate. Here, BomberPlane stands back and observes.
   BomberPlane then repeats steps 2 and 3 indefinitely.
   Note that during every second BomberPlane plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of BomberPlane's first batch of planted bombs, determine the state of the grid after n seconds.

For example, if the initial grid looks like:
['...', '.O.', '...']
After 1 second: ['...', '.O.', '...']
After 2 seconds: ['OOO', 'OOO', 'OOO']. To help my understanding for this problem, I thought of this as: ['111', '121', '111'] where the integer is the number of seconds passed since the bomb was planted
After 3 seconds: ['O.O', '...', 'O.O'] because the '2' has just detonated, clearing its neighbouring cells
After 4 seconds: ['OOO', 'OOO', 'OOO'] or in seconds since planting: ['212', '111', '212']
After 5 seconds: ['...', '.O.', '...']
After 7 seconds: ['O.O', '...', 'O.O']
After 9 seconds: ['...', '.O.', '...']
After 11 seconds: ['O.O', '...', 'O.O']
After 13 seconds: ['...', '.O.', '...']

I noticed there is a recurring pattern. After 5, 9, 13, 17 etc (n % 4 = 1), the grid is always the same. After 3, 7, 11, 15(n%4=3), the grid is always the same. So really there are only ever going to be 4 states:

- n < 2, grid is the initial grid, because bomberplane does nothing until 2 seconds have passed
- Because every 2 seconds, bomberplane fills the grid with bombs, when n is even (n%2=0), the grid is always a grid of Os
- Grid at n % 4 = 3 will always be the same as grid_after_3_seconds
- Grid at n % 4 = 1 will always be the same as grid_after_5_seconds, which can be worked out from looking at grid_after_3_seconds
