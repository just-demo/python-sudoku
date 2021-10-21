import math
from value import Value
from cell import Cell
from errors import *
from format import *


class Solver:
    def __init__(self, initial_state):  # int[][]
        self.size = len(initial_state)
        self.all_cells = []
        self.pending_cells = []
        self.pending_values = []
        box_size = int(math.sqrt(self.size))
        all_values = list(map(lambda v: Value(self.pending_values, self.size, v + 1), range(self.size)))
        open_cells = []  # [(Cell, Value)]
        for row in range(self.size):
            for col in range(self.size):
                box = box_size * (row // box_size) + col // box_size
                cell = Cell(self.pending_cells, row, col, box)
                self.all_cells.append(cell)
                value = initial_state[row][col]
                if value:
                    open_cells.append((cell, all_values[value - 1]))
        self.pending_cells.extend(self.all_cells)
        self.pending_values.extend(all_values)
        for cell in self.pending_cells:
            cell.add_candidate_values(self.pending_values)
        for value in self.pending_values:
            value.add_candidate_cells(self.pending_cells)
        for cell, value in open_cells:
            cell.open_candidate_value(value)

    def solve(self):
        while self.pending_cells:
            try:
                self.__open_next()
            except CannotOpenWithoutGuessingException as e:
                return self.__solve_with_guess(e.cell, e.value)
        return self.__copy_state()

    def __copy_state(self):
        state = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for cell in self.all_cells:
            if cell.value:
                state[cell.row][cell.col] = cell.value.value
        return state

    def __open_next(self):
        if not self.pending_values:
            raise NoSolutionException()

        cell = min(self.pending_cells, key=lambda c: c.count_candidate_values())
        if cell.try_open_single_candidate_value():
            return

        value = min(self.pending_values, key=lambda v: v.count_candidate_cells())
        if value.try_open_single_candidate_cell():
            return

        if cell.has_candidate_values() and value.has_candidate_cells():
            raise CannotOpenWithoutGuessingException(cell, value)
        # print(sudoku_to_2d_string(self.__copy_state()))
        # print(str(value.value) + ': ' + str(cell.row) + ' - ' + str(cell.col))
        raise NoSolutionException()

    def __solve_with_guess(self, cell, value):
        if cell.count_candidate_values() > value.count_candidate_cells():
            guess_cells = value.get_candidate_cells()
            guess_values = [value]
        else:
            guess_cells = [cell]
            guess_values = cell.get_candidate_values()
        solutions = []
        for guess_cell in guess_cells:
            for guess_value in guess_values:
                guess_state = self.__copy_state()
                guess_state[guess_cell.row][guess_cell.col] = guess_value.value
                try:
                    solutions.append(Solver(guess_state).solve())
                    if len(solutions) > 1:
                        raise MultipleSolutionsException()
                except NoSolutionException:
                    # Our guess did not work, let's try another one
                    pass
        if not solutions:
            raise NoSolutionException
        return solutions[0]
