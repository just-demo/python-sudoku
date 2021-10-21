class Cell:
    def __init__(self, pending_cells, row, col, box):
        self.pending_cells = pending_cells
        self.row = row
        self.col = col
        self.box = box
        self.value = None
        self.candidate_values = []

    def add_candidate_values(self, values):  # Value[]
        self.candidate_values.extend(values)

    def open_candidate_value(self, value):
        self.value = value
        for val in self.candidate_values:
            val.remove_candidate_cell(self)
        self.candidate_values.clear()
        value.open_candidate_cell(self)
        self.pending_cells.remove(self)
        for cell in self.pending_cells:
            if self.is_competitor(cell):
                cell.remove_candidate_value(value)

    def is_competitor(self, cell):
        return self.row == cell.row or self.col == cell.col or self.box == cell.box

    def remove_candidate_value(self, value):
        value.remove_candidate_cell(self)
        if value in self.candidate_values:
            self.candidate_values.remove(value)

    def has_candidate_values(self):
        return bool(self.candidate_values)

    def count_candidate_values(self):
        return len(self.candidate_values)

    def try_open_single_candidate_value(self):
        if len(self.candidate_values) == 1:
            self.open_candidate_value(self.candidate_values[0])
            return True
        return False

    def get_candidate_values(self):
        return self.candidate_values
