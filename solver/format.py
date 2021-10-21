import math


def sudoku_from_2d_string(string):
    return [[cell_from_string(value) for value in line.split()] for line in string.split('\n') if line]


def sudoku_to_2d_string(sudoku):
    return '\n'.join([' '.join([str(value) if value else '.' for value in line]) for line in sudoku])


def cell_from_string(string):
    return int(string) if string.isdigit() else 0


def sudoku_from_1d_string(string):
    size = int(math.sqrt(len(string)))
    return [[cell_from_string(string[row * size + col]) for col in range(size)] for row in range(size)]
