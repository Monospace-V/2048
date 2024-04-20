class grid:
    def __init__(self, size = 4):
        self.size = size
        rows = []
        for row in range(size):
            rows.append([0] * size)
        self.rows = rows
        self.columns = columnize(self.rows)
    def vertical(self, reverse = False):
        out = []
        for column in self.columns:
            if reverse: column = column[::-1]
            out.append(column)
        return out
    def horizontal(self, reverse = False):
        out = []
        for row in self.rows:
            if reverse: row = row[::-1]
            out.append(row)
        return out
    def update(self,rows):
        self.rows = rows
        self.columns = columnize(rows)

def columnize(rows):
    columns = []
    for col_pos in range(size):
        column = []
        for row in rows:
            column.append(row[col_pos])
        columns.append(column)
    return columns


def swipe_down(grid):
    columns = grid.vertical(reverse = True)
    