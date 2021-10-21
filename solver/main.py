from solver import Solver
from format import *
import time

sudoku1 = '''
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
'''

sudoku2 = '.......9......8.2.7.3.54.....52.................6....88....3..7.9....6..6...8...4'
'''
1 4 8 3 2 6 7 9 5
5 6 9 7 1 8 4 2 3
7 2 3 9 5 4 8 1 6
4 8 5 2 3 7 1 6 9
9 3 6 8 4 1 5 7 2
2 7 1 6 9 5 3 4 8
8 1 2 4 6 3 9 5 7
3 9 4 5 7 2 6 8 1
6 5 7 1 8 9 2 3 4
'''
# sudoku = sudoku_from_2d_string(sudoku1)
sudoku = sudoku_from_1d_string(sudoku2)
print(sudoku_to_2d_string(sudoku))
start = time.time_ns()
solver = Solver(sudoku)
solution = solver.solve()
print(f'Time: {(time.time_ns() - start) / 1000000000}')
print(sudoku_to_2d_string(solution))
