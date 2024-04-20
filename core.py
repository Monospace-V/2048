class grid:
    def __init__(self, size = 4):
        self.size = size
        rows = []
        for row in range(size):
            rows.append([0] * size)
        self.rows = rows
        columns = []
        for col_pos in range(size):
            column = []
            for row in self.rows:
                column.append(row[col_pos])
            columns.append(column)
        self.columns = columns
    def down(self): # Returns wrt bottom. Weigh toward start of list.
        out=[]
        for column in self.columns:
            out.append(column[::-1])
        return out
    def up(self):
        return self.columns
    def left(self):
        return self.rows
    def right(self):
        out=[]
        for row in self.rows:
            out.append(row[::-1])
        return out