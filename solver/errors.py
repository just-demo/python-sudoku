class NoSolutionException(Exception):
    pass


class MultipleSolutionsException(Exception):
    pass


class CannotOpenWithoutGuessingException(Exception):
    def __init__(self, cell, value):
        self.cell = cell
        self.value = value
