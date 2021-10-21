from collections import defaultdict


class Value:
    def __init__(self, pending_values, target_open_cells_count, value):
        self.pending_values = pending_values
        self.target_open_cells_count = target_open_cells_count
        self.value = value
        self.open_cells = []
        self.candidate_cell_groups = []

    def add_candidate_cells(self, cells):
        self.candidate_cell_groups.extend(self.__group_by(cells, lambda cell: cell.row))
        self.candidate_cell_groups.extend(self.__group_by(cells, lambda cell: cell.col))
        self.candidate_cell_groups.extend(self.__group_by(cells, lambda cell: cell.box))

    def __group_by(self, items, group_key_func):
        groups = defaultdict(list)
        for item in items:
            groups[group_key_func(item)].append(item)
        return list(groups.values())

    def remove_candidate_cell(self, cell):
        for cells in self.candidate_cell_groups:
            if cell in cells:
                cells.remove(cell)
                if not cells:
                    self.candidate_cell_groups.remove(cells)

    def open_candidate_cell(self, cell):
        self.remove_candidate_cell(cell)
        self.open_cells.append(cell)
        if len(self.open_cells) == self.target_open_cells_count:
            self.pending_values.remove(self)

    def get_candidate_cells(self):
        return min(self.candidate_cell_groups, key=lambda cells: len(cells)) if self.candidate_cell_groups else []

    def has_candidate_cells(self):
        return bool(self.candidate_cell_groups)

    def count_candidate_cells(self):
        return min(len(cells) for cells in self.candidate_cell_groups) if self.candidate_cell_groups else 0

    def try_open_single_candidate_cell(self):
        cells = self.get_candidate_cells()
        if len(cells) == 1:
            self.open_candidate_cell(cells[0])
            return True
        return False